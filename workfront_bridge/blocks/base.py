from workfront.objects import project as wf_project
from workfront.objects.codes import WFObjCode
from workfront_bridge.exceptions import WFBrigeException
import uuid


class WFBlockAttrib(object):
    def __init__(self, task_identifier, field, alias, formatter=None):
        self.task_identifier = task_identifier
        self.field = field
        self.alias = '_' + alias
        self.formatter = formatter or str

    def check_is_block(self, instance):
        if instance is None or not isinstance(instance, WFBlock):
            raise AttributeError('WFBlockAttrib must be '
                                 'exeucte on a WFBlock instance level')

    def __get__(self, block, _):
        self.check_is_block(block)
        return getattr(
            self,
            self.alias,
            block.parameters.get(
                self.task_identifier,
                {},
            ).get(
                self.field,
                None
            )
        )

    def __set__(self, block, value):
        self.check_is_block(block)
        if value is not None:
            setattr(self, self.alias, value)
            block.set_parameter(self.task_identifier, self.field, self.formatter(value))


class WFBlockMeta(type):
    '''
    Metaclass helper to create getter/setter for a given mapping of workfront attributes

    class MyBlock(WFBlock):
        block_params = {
            # taks name or an emtpy string for block attributes
            '': (
                # list of mapping attributes (WF field, class property name, requried[, formatter])
                ('Project Type', 'project_type', True),
            ),
            'task 1': (
                ('S3 Path', 'path', False, lambda l: ','.join(l)),
            ),
        }
    '''
    def __new__(cls, name, bases, dct):
        block_cls = super(WFBlockMeta, cls).__new__(cls, name, bases, dct)

        # create block properties based on the given alias
        block_params = getattr(block_cls, 'block_params', {})
        if block_params:
            for task_name, parameters in block_params.iteritems():
                for group in parameters:
                    formatter = str
                    param, alias, _ = group[:3]
                    formatter = group[3] if len(group) > 3 else str
                    setattr(block_cls, alias, WFBlockAttrib(task_name, param, alias, formatter))

        # extend block_params attribute with the base classes
        for base in bases:
            base_parameters = getattr(base, 'block_params', None)
            if base_parameters:
                for task_name, parameters in base_parameters.iteritems():
                    if task_name in block_params:
                        block_params[task_name] = tuple(block_params[task_name]) + tuple(parameters)
                    else:
                        block_params[task_name] = parameters
        block_cls.block_params = block_params

        return block_cls


class WFBlock(object):
    '''
    @summary: Workfront Base Block class
    '''
    __metaclass__ = WFBlockMeta

    def __init__(self, wf_template_name=None, name=None):
        '''
        @param wf: a Workfront service object.
        @param wf_template_id: workfront template id that will be instantiated
        by this block.
        '''
        self.name = name
        self.blocks = []
        self.wf_template_name = wf_template_name or getattr(self, 'template_name', None)
        self.parameters = {}
        self.starter_task_identifier = None
        self._set_starter_task(1)  # default to first task

        assert self.wf_template_name, ('wf_template_name and/or template_name '
                                       'missing on {}'.format(self.__class__.__name__))

    def set_parameter(self, task_identifier, field, value):
        '''
        @summary: Set the value to the given field for the specified task of
        this block object.
        @param task_identifier: task identifier. The task identifier must
        uniquely identify one of the tasks of the current block.
        The identifier can be:
        - An int: In which case is the number of the task in the block (from 1
        to N).
        - A string: In which case it must match the name of one of the tasks of
        the blocks.
        @param field: parameter value field name.
        @param value: value of the parameter field.
        '''
        if value is None:
            return
        if task_identifier not in self.parameters:
            self.parameters[task_identifier] = {}
        self.parameters[task_identifier][field] = value

    def iter_block_params(self):
        all_params = getattr(self, 'block_params', None)
        if not all_params:
            return

        for task_name, task_params in all_params.iteritems():
            for parms in task_params:
                name, alias, required = parms[:3]
                yield task_name, name, alias, required

    @property
    def required_parameters(self):
        return [
            name
            for _, name, _, required in self.iter_block_params()
            if required
        ]

    @property
    def optional_parameters(self):
        return [
            name
            for _, name, _, required in self.iter_block_params()
            if not required
        ]

    def check_parameters(self):
        '''
        @summary: Check that all the parameters given, match the ones set as
        required and optional for this block.
        @raise WFBridgeException: if there is a mismatch with the parameters.
        '''
        all_params = set(
            param
            for pv in self.parameters.itervalues()
            for param in pv.iterkeys()
        )

        req = set(self.required_parameters)
        opt = set(self.optional_parameters)

        # Check all required parameters are set
        if not req.issubset(all_params):
            missing = ",".join(req - all_params)
            err = "Missing required parameters {} for {}".format(
                missing, type(self).__name__,
            )
            raise WFBrigeException(err)

        # Now check that the parameters that are not required are optional
        if not (all_params - req).issubset(opt):
            unused_parameters = ",".join(all_params - req - opt)
            err = "{} have been specified but are not required nor optional for {}".format(
                unused_parameters, type(self).__name__,
            )
            raise WFBrigeException(err)

        for block in self.blocks:
            block.check_parameters()

    def _set_starter_task(self, task_identifier):
        '''
        @param task_identifier: a "task identifier" as defined in method
        set_task_param_value (int or string).
        '''
        self.starter_task_identifier = task_identifier

    def append(self, child_block):
        self.blocks.append(child_block)


class WFBlockParser(object):

    def __init__(self, wf):
        self.wf = wf
        self._indented_tasks = []
        self._starter_task_base_level = 2

    def _get_temporal_project_name(self, prefix="Generic"):
        '''
        @return: unique name of a project block
        '''
        uid = uuid.uuid4()
        pname = "Temporary Block {} - {}".format(prefix, uid)
        return pname

    def create(self, wf_block):
        """
        :type wf_block: WFBlock
        """
        wf_block.check_parameters()

        template_id = self.template_id_from_name(wf_block.wf_template_name)
        prj = wf_project.crt_from_template(self.wf, template_id, wf_block.name)
        if "" in wf_block.parameters:
            prj.set_param_values(wf_block.parameters[""])

        for block in wf_block.blocks:
            self.attach_to_project(prj, block)

        return prj

    def attach_to_project(self, project, block_to_attach, indent=False):
        """Attach block to project"""

        prj_tasks = project.get_tasks()
        predecessor_task = None
        if len(prj_tasks) > 0:
            predecessor_task = prj_tasks[len(prj_tasks) - 1]
        block_project = self.__create_project_from(block_to_attach)
        if block_to_attach.blocks:
            # Sub-block indentation
            starter_task = self._starter_task_base_level
            first_block_blocks = block_to_attach.blocks[0].blocks
            while first_block_blocks:
                starter_task += 1
                if not first_block_blocks[0].blocks:
                    break
                first_block_blocks = first_block_blocks[0].blocks
            block_to_attach._set_starter_task(starter_task)
            [self.attach_to_project(block_project, child_block, indent=True) for child_block in block_to_attach.blocks]

        block_tasks = block_project.get_tasks()
        project.move_into(block_tasks)
        if indent:
            first_task_id = prj_tasks[0].wf_id
            for task in block_tasks:
                if task.wf_id not in self._indented_tasks:
                    task.set_fields({"parentID": first_task_id})
                    self._indented_tasks.append(task.wf_id)
        if predecessor_task:
            # get the first task that needs to have a predecessor, this is to
            # avoid non automatic block task not starting. So in general, you
            # would like to have the first automatic task as a starter task
            task = self.__task_from_name(block_to_attach.starter_task_identifier,
                                         block_tasks, project)
            task.add_predecessor(predecessor_task)
        block_project.delete()

    def __create_project_from(self, block):
        name = self._get_temporal_project_name(block.__class__.__name__)

        template_id = self.template_id_from_name(block.wf_template_name)
        prj = wf_project.crt_from_template(self.wf, template_id, name)
        tasks = prj.get_tasks()

        for task_identif, param_values in block.parameters.iteritems():
            task = self.__task_from_name(task_identif, tasks, prj)
            task.set_param_values(param_values)
        return prj

    def __task_from_name(self, task_name, tasks, prj):
        # Task identifier is a task number in the project block
        if type(task_name) == int:
            if len(tasks) < task_name:
                tmpl = prj.get_template_id()
                err = "Project Template {} has {} tasks. Task {} referenced " \
                      "from task parameter values."
                err = err.format(tmpl, len(tasks), task_name)
                raise WFBrigeException(err)
            return tasks[task_name - 1]

        # Task is being identified by its name
        mtasks = [t for t in tasks if t.name == task_name]
        if len(mtasks) == 1:
            return mtasks[0]
        elif len(mtasks) == 0:
            tmpl = prj.get_template_id()
            err = "Project Template {} does not have task name {} referenced " \
                  "from task parameter values."
            err = err.format(tmpl, task_name)
            raise WFBrigeException(err)
        else:
            tmpl = prj.get_template_id()
            err = "Project Template {} has more than one task named as {}"
            err = err.format(tmpl, task_name)
            raise WFBrigeException(err)

    def template_id_from_name(self, name):
        '''
        @return: A WF project template id corresponding to the template project
        name given.
        @param wf: a Workfront service object.
        @param name: name of the project template.
        '''

        r = self.wf.search_objects(WFObjCode.templat_project, {"name": name})
        if len(r.json()["data"]) != 1:  # not found
            raise WFBrigeException("WF Template '{}' not found".format(name))
        return r.json()["data"][0]["ID"]
