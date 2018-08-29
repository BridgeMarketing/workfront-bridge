from workfront.objects import project as wf_project
from workfront.objects.codes import WFObjCode
from workfront_bridge.exceptions import WFBrigeException
import uuid



class WFBlock(object):
    '''
    @summary: Workfront Base Block class
    '''

    def __init__(self, wf_template_name, name=None):
        '''
        @param wf: a Workfront service object.
        @param wf_template_id: workfront template id that will be instantiated
        by this block.
        '''
        self.name = name
        self.blocks = []
        self.wf_template_name = wf_template_name
        self.parameters = {}
        self.required_parameters = []
        self.optional_parameters = []
        self.starter_task_identifier = None
        self._set_starter_task(1)  # default to first task

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

    def _add_required_parameters(self, fields):
        '''
        @param fields: The given fields are marked as mandatory for this block.
        '''
        self.required_parameters.extend(fields)

    def _add_optional_parameters(self, fields):
        '''
        @param fields: The given fields are marked as optional for this block.
        '''
        self.optional_parameters.extend(fields)

    def check_parameters(self):
        '''
        @summary: Check that all the paramenters given, match the ones set as
        required and optional for this block.
        @raise WFBridgeExcepion: if there is a mismatch with the parameters.
        '''
        all_params = []
        for pv in self.parameters.itervalues():
            all_params.extend(pv.keys())
        all_params = set(all_params)

        req = set(self.required_parameters)
        opt = set(self.optional_parameters)

        # Check all required parameters are set
        if not req.issubset(all_params):
            missing = ",".join(req - all_params)
            err = "Missing required parameters {}".format(missing)
            raise WFBrigeException(err)

        # Now check that the parameters that are not required are optional
        if not (all_params - req).issubset(opt):
            unused_parameters = ",".join(all_params - req - opt)
            err = "{} have been specified but are not required nor optional"
            raise WFBrigeException(err.format(unused_parameters))

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

        template_id = self.template_id_from_name( wf_block.wf_template_name)
        prj = wf_project.crt_from_template(self.wf, template_id, wf_block.name)
        prj.set_param_values(wf_block.parameters[""])

        for block in wf_block.blocks:
            self.attach_to_project(prj, block)

        return prj

    def attach_to_project(self, project, block_to_attach):
        prj_tasks = project.get_tasks()
        predecessor_task = None
        if len(prj_tasks) > 0:
            predecessor_task = prj_tasks[len(prj_tasks) - 1]

        block_project = self.__create_project_from(block_to_attach)
        tasks = block_project.get_tasks()
        project.move_into(tasks)

        if predecessor_task:
            # get the first task that need to have a predecessor, this is to
            # avoid non automatic block task not starting. So in general, you
            # would like to have the first automatic task as a starter task
            task = self.__task_from_name(block_to_attach.starter_task_identifier,
                                         tasks, project)
            task.add_predecessor(predecessor_task)

        block_project.delete()

    def __create_project_from(self, block):
        name = self._get_temporal_project_name(block.__class__.__name__)

        template_id = self.template_id_from_name( block.wf_template_name)
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
                tmpl = prj.get_template()
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
            tmpl = prj.get_template()
            err = "Project Template {} does not have task name {} referenced " \
                  "from task parameter values."
            err = err.format(tmpl, task_name)
            raise WFBrigeException(err)
        else:
            tmpl = prj.get_template()
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
        return r.json()["data"][0]["ID"]