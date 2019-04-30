from workfront.objects.project import WFProject

from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.projects.cancel import WFProjectCancelContainer

from workfront_bridge.blocks.cancel import WFCancelEmailDeployBlock


class CancelProjectBuilder(object):
    '''
    @summary: Cancel project builder to easily construct Cancel workfront
    projects to cancel other workfront projects.
    '''

    def __init__(self, wf):
        '''
        @param wf: Workfront service object
        '''
        self.supported_project_types = {
            "Email": self.__build_cancel_email_deploy,
        }
        self.wf = wf

        self.wf_project_id = None
        self.project_type = None  # Project type being cancelled

    def get_supported_project_types(self):
        '''
        @return: A list of Project Types that can be cancelled using this
        builder.
        '''
        return self.supported_project_types.keys()

    def set_project_to_cancel(self, wf_project_id):
        '''
        @param wf_project_id: id of the wf project to cancel
        '''
        self.wf_project_id = wf_project_id
        return self

    def _check_viability(self):
        '''
        @summary: Check if all the requirement parameters of the builder are
        set in order to build a cancel project.
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
        cancel (self.wf_project_id)
        @raise WFBridgeException: if the project has an unsupported project
        type to cancel.
        '''
        prj = WFProject(self.wf, self.wf_project_id)
        params = prj.get_param_values()
        if "Project Type" not in params:
            WFBrigeException("Unknown Project Type - {} is missing Project "
                             "Type custom form field".format(prj))
        if params["Project Type"] not in self.supported_project_types:
            WFBrigeException("Project Type {} not supported for canceling "
                             "project {}".format(prj))
        self.project_type = params["Project Type"]

    def __build_cancel_email_deploy(self):
        '''
        @return: a cancel wf project to cancel an email project.
        '''
        # Mark the project as cancel
        prj_being_cancelled = WFProject(self.wf, self.wf_project_id)
        prj_being_cancelled.set_param_values({"isCancel": "yes"})

        prj_name = "Cancel - {}".format(prj_being_cancelled.name)
        project = WFProjectCancelContainer(prj_name)
        cancel_block = WFCancelEmailDeployBlock()
        cancel_block.project_id = self.wf_project_id
        project.append(cancel_block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        # Set dependencies to Avoid raise conditions
        try:
            # Get Audience Live Setup Push to Provider Task
            tasks = prj_being_cancelled.get_tasks()
            aud_tsk = [t for t in tasks if t.name == "Audience Live Setup"][0]
            aud_tasks = tasks[tasks.index(aud_tsk):]
            ptp_task = [t for t in aud_tasks if t.name == "Push to provider"][0]

            # Now link the cancel task to the push to proivder one
            cancel_task = wf_project.get_tasks()[0]
            cancel_task.add_predecessor(ptp_task)
        except Exception:
            pass

        return wf_project

    def build(self):
        '''
        @summary: According to all the parameters set to the builder, build a
        workfront cancel project.
        @raise WFBrigeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        '''
        self._check_viability()

        # Call the corresponding method to create the cancel project
        return self.supported_project_types[self.project_type]()
