from workfront.objects import project as wf_project
from workfront.objects.codes import WFObjCode
from workfront_bridge.exceptions import WFBrigeException
import uuid


def template_id_from_name(wf, name):
    '''
    @return: A WF project template id corresponding to the template project
    name given.
    @param wf: a Workfront service object.
    @param name: name of the project template.
    '''
    r = wf.search_objects(WFObjCode.templat_project, {"name": name})
    return r.json()["data"][0]["ID"]


class WFBlock(object):
    '''
    @summary: Workfront Base Block class
    '''

    def __init__(self, wf, wf_template_id):
        '''
        @param wf: a Workfront service object.
        @param wf_template_id: workfront template id that will be instantiated
        by this block.
        '''
        self.wf = wf
        self.wf_template_id = wf_template_id
        self.task_params = {}
        self.req_fields = []
        self.opt_fields = []

    def __temp_name(self):
        '''
        @return: unique name of a project block
        '''
        uid = uuid.uuid4()
        pname = "Temporary Block {} - {}".format(self.__class__.__name__, uid)
        return pname

    def __task_from_indentifier(self, task_identif, tasks, prj):
        '''
        @return: a WFTask from the tasks list that matchs the task_identif
        @param task_identif: A string or int that identifies one task.
        In the case of the int, it is the index of the tasks list.
        In the case of the string, it is the name of the task.
        @raise WFBridgeException: This exception will be raise if the task can
        not be uniquely identify.
        '''

        # Task identifier is a task number in the project block
        if type(task_identif) == int:
            if len(tasks) < task_identif:
                tmpl = prj.get_template()
                err = "Project Template {} has {} tasks. Task {} referenced "\
                      "from task parameter values."
                err = err.format(tmpl, len(tasks), task_identif)
                raise WFBrigeException(err)
            return tasks[task_identif - 1]

        # Task is being identified by its name
        mtasks = [t for t in tasks if t.name == task_identif]
        if len(mtasks) == 1:
            return mtasks[0]
        elif len(mtasks) == 0:
            tmpl = prj.get_template()
            err = "Project Template {} does not have task name {} referenced "\
                  "from task parameter values."
            err = err.format(tmpl, task_identif)
            raise WFBrigeException(err)
        else:
            tmpl = prj.get_template()
            err = "Project Template {} has more than one task named as {}"
            err = err.format(tmpl, task_identif)
            raise WFBrigeException(err)

    def __create_project(self):
        '''
        @summary: Create a project from the template of this block and fullfill
        all its tasks parameter values with the task_params dictionary.
        @return: a new WFProject object.
        '''
        name = self.__temp_name()
        prj = wf_project.crt_from_template(self.wf, self.wf_template_id, name)
        tasks = prj.get_tasks()
        for task_identif, param_values in self.task_params.iteritems():
            task = self.__task_from_indentifier(task_identif, tasks, prj)
            task.set_param_values(param_values)
        return prj

    def attach_to_project(self, prj):
        '''
        @summary: Create tasks of the current block into the given project.
        Internally, this method instantiates a project corresponding to this
        block and move all the tasks into the given project.
        After that it erases the created project.
        '''
        prj_tasks = prj.get_tasks()
        predecessor_task = None
        if len(prj_tasks) > 0:
            predecessor_task = prj_tasks[len(prj_tasks)-1]

        block_project = self.__create_project()
        tasks = block_project.get_tasks()
        prj.move_into(tasks)

        if predecessor_task:
            tasks[0].add_predecessor(predecessor_task)

        block_project.delete()

    def set_task_param_value(self, task_identifier, field, value):
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
        if task_identifier not in self.task_params:
            self.task_params[task_identifier] = {}
        self.task_params[task_identifier][field] = value

    def _set_required_fields(self, fields):
        '''
        @param fields: The given fields are marked as mandatory for this block.
        '''
        self.req_fields.extend(fields)

    def _set_optional_fields(self, fields):
        '''
        @param fields: The given fields are marked as optional for this block.
        '''
        self.opt_fields.extend(fields)

    def _check_param_values(self):
        '''
        @summary: Check that all the paramenters given, match the ones set as
        required and optional for this block.
        @raise WFBridgeExcepion: if there is a mismatch with the parameters.
        '''
        all_params = []
        for pv in self.task_params.itervalues():
            all_params.extend(pv.keys())
        all_params = set(all_params)

        req = set(self.req_fields)
        opt = set(self.opt_fields)

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


class WFProjectBlock(object):

    def __init__(self, wf, wf_template_id, prj_name):
        '''
        @param wf: a Workfront service object.
        @param wf_template_id: workfront template id that will be instantiated
        by this project block.
        @param prj_name: Name of the project that will be created.
        '''
        self.wf = wf
        self.wf_template_id = wf_template_id
        self.prj_name = prj_name
        self.blocks = []
        self.param_values = {}
        self.opt_fields = []
        self.req_fields = []

    def append(self, block):
        '''
        @summary: Append a WF block to this project block. Blocks are being
        chained so that every block will execute only when the predecessor
        block is finished.
        Blocks are being chained in the order that they are being append.
        @param block: a WFBlock object
        '''
        self.blocks.append(block)

    def create(self):
        '''
        @return: a WFProject object with all the parameters set on it and with
        all the WF blocks appended (with its parameters set).
        @raise WFBrigeException: when a field of the project or from any block
        is missing.
        '''
        self._check_param_values()
        for block in self.blocks:
            self._check_param_values()

        prj = wf_project.crt_from_template(self.wf, self.wf_template_id,
                                           self.prj_name)
        prj.set_param_values(self.param_values)

        for block in self.blocks:
            block.attach_to_project(prj)

        return prj

    def _set_required_fields(self, fields):
        '''
        @param fields: The given fields are marked as mandatory for this
        project block.
        '''
        self.req_fields.extend(fields)

    def _set_optional_fields(self, fields):
        '''
        @param fields: The given fields are marked as optional for this
        project block.
        '''
        self.opt_fields.extend(fields)

    def set_param_value(self, field, value):
        '''
        @param field: project parameter value field name.
        @param value: project value of the parameter field.
        '''
        self.param_values[field] = value

    def _check_param_values(self):
        '''
        @summary: Check that all the paramenters given, match the ones set as
        required and optional for this project block.
        @raise WFBridgeExcepion: if there is a mismatch with the parameters.
        '''
        all_params = set(self.param_values.keys())

        req = set(self.req_fields)
        opt = set(self.opt_fields)

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
