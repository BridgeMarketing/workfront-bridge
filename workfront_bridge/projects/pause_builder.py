from workfront.objects.project import WFProject

from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.blocks.pause import WFPauseEmailDeployBlock
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.projects.pause import WFProjectPauseContainer


class PauseProjectBuilder(object):
    '''
    @summary: Pause project builder to easily construct Pause workfront
    projects to pause other workfront projects.
    '''

    def __init__(self, wf):
        '''
        @param wf: Workfront service object
        '''
        self.supported_project_types = {
            "Email": self.__build_pause_email_deploy,
        }
        self.wf = wf

        self.wf_project_id = None
        self.project_type = None  # Project type being paused

    def get_supported_project_types(self):
        '''
        @return: A list of Project Types that can be paused using this
        builder.
        '''
        return self.supported_project_types.keys()

    def set_project_to_pause(self, wf_project_id):
        '''
        @param wf_project_id: id of the wf project to pause
        '''
        self.wf_project_id = wf_project_id
        return self

    def _check_viability(self):
        '''
        @summary: Check if all the requirement parameters of the builder are
        set in order to build a pause project.
        '''
        def check_not_none(name, value):
            if value is None:
                raise WFBrigeException("{} is required".format(name))

        check_not_none("wf_project_id", self.wf_project_id)
        self.__fullfill_project_type()
        check_not_none("project_type", self.project_type)

    def __fullfill_project_type(self):
        '''
        @summary: Fullfill self.project_type based on the project that will be
        pause (self.wf_project_id)
        @raise WFBridgeException: if the project has an unsupported project
        type to pause.
        '''
        prj = WFProject(self.wf, self.wf_project_id)
        params = prj.get_param_values()
        if "Project Type" not in params:
            WFBrigeException("Unknown Project Type - {} is missing Project "
                             "Type custom form field".format(prj))
        if params["Project Type"] not in self.supported_project_types:
            WFBrigeException("Project Type {} not supported for pausing "
                             "project {}".format(prj))
        self.project_type = params["Project Type"]

    def __build_pause_email_deploy(self):
        '''
        @return: a pause wf project to pause an email project.
        '''

        prj_being_paused = WFProject(self.wf, self.wf_project_id)

        prj_name = "Pause - {}".format(prj_being_paused.name)
        project = WFProjectPauseContainer(prj_name)
        pause_block = WFPauseEmailDeployBlock()
        pause_block.project_id = self.wf_project_id
        project.append(pause_block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        # Set dependencies to Avoid raise conditions
        try:
            # Get Audience Live Setup Push to Provider Task
            tasks = prj_being_paused.get_tasks()
            aud_tsk = [t for t in tasks if t.name == "Audience Live Setup"][0]
            aud_tasks = tasks[tasks.index(aud_tsk):]
            ptp_task = [t for t in aud_tasks if t.name == "Push to provider"][0]

            # Now link the pause task to the push to proivder one
            pause_task = wf_project.get_tasks()[0]
            pause_task.add_predecessor(ptp_task)
        except Exception:
            pass

        return wf_project

    def build(self):
        '''
        @summary: According to all the parameters set to the builder, build a
        workfront pause project.
        @raise WFBrigeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        '''
        self._check_viability()

        # Call the corresponding method to create the pause project
        return self.supported_project_types[self.project_type]()
