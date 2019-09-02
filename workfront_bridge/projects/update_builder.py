from workfront.objects.project import WFProject

from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.projects.update import WFProjectUpdateContainer

from workfront_bridge.blocks.update import WFUpdateEmailDeployBlock
from workfront_bridge.tools import datetime_to_wf_format


class UpdateProjectBuilder(object):
    '''
    @summary: Update project builder to easily construct Update workfront
    projects to update other workfront projects.
    '''

    def __init__(self, wf):
        '''
        @param wf: Workfront service object
        '''
        self.supported_project_types = {
            "Email": self.__build_update_email_deploy,
        }
        self.wf = wf

        self.wf_project_id = None
        self.deploy_datetime = None
        self.project_type = None  # Project type being updateled

    def get_supported_project_types(self):
        '''
        @return: A list of Project Types that can be updateled using this
        builder.
        '''
        return self.supported_project_types.keys()

    def set_project_to_update(self, wf_project_id):
        '''
        @param wf_project_id: id of the wf project to update
        '''
        self.wf_project_id = wf_project_id
        return self

    def set_datetime_to_update(self, dt):
        '''
        @param dt: deploy datetime to update
        '''
        self.deploy_datetime = dt
        return self

    def _check_viability(self):
        '''
        @summary: Check if all the requirement parameters of the builder are
        set in order to build a update project.
        '''

        def check_not_none(name, value):
            if value is None:
                raise WFBrigeException("{} is required".format(name))

        check_not_none("wf_project_id", self.wf_project_id)
        check_not_none("deploy_datetime", self.deploy_datetime)
        self.__fullfill_project_type()
        check_not_none("project_type", self.project_type)

    def __fullfill_project_type(self):
        '''
        @summary: Fullfill self.project_type based on the project that will be
        update (self.wf_project_id)
        @raise WFBridgeException: if the project has an unsupported project
        type to update.
        '''
        prj = WFProject(self.wf, self.wf_project_id)
        params = prj.get_param_values()
        if "Project Type" not in params:
            WFBrigeException("Unknown Project Type - {} is missing Project "
                             "Type custom form field".format(prj))
        if params["Project Type"] not in self.supported_project_types:
            WFBrigeException("Project Type {} not supported for updating "
                             "project {}".format(prj))
        self.project_type = params["Project Type"]

    def __build_update_email_deploy(self):
        '''
        @return: a update wf project to update an email project.
        '''
        prj_being_updated = WFProject(self.wf, self.wf_project_id)

        program = prj_being_updated.get_program()
        all_project = program.get_projects()

        cw_tool_projects = [p for p in all_project if p.name.startswith("CW tool")]

        tarjeted_bonus_media_projects = [p for p in all_project if p.name.startswith("TBM - ")]

        prj_name = "Update - {}".format(prj_being_updated.name)
        project = WFProjectUpdateContainer(prj_name)
        update_block = WFUpdateEmailDeployBlock()
        update_block.project_id = self.wf_project_id
        update_block.deploy_datetime = self.deploy_datetime
        project.append(update_block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        # Get Audience Live Setup Push to Provider Task
        tasks = prj_being_updated.get_tasks()
        aud_tsk = [t for t in tasks if t.name == "Audience Live Setup"][0]
        aud_tasks = tasks[tasks.index(aud_tsk):]
        ptp_task = [t for t in aud_tasks if t.name == "Push to provider"][0]

        # # Now link the update task to the push to proivder one
        # update_task = wf_project.get_tasks()[0]
        # update_task.add_predecessor(ptp_task)

        # Update Audience "Deployment Date/Time" parameter with the new deploy_datetime
        create_flight_task = [t for t in aud_tasks if t.name == "Create Flight"][0]
        create_flight_task.set_param_values({"Deployment Date/Time": datetime_to_wf_format(self.deploy_datetime)})

        # Update Live Setup "Deployment Date/Time" parameter with the new deploy_datetime
        live_setup_task = [t for t in tasks if t.name == "Live Setup"][0]
        live_setup_task_tasks = tasks[tasks.index(live_setup_task):]

        live_setup_create_flight_task = [t for t in live_setup_task_tasks if t.name == "Create Flight"][0]
        live_setup_create_flight_task.set_param_values(
            {"Deployment Date/Time": datetime_to_wf_format(self.deploy_datetime)})

        # Update "Start Date" in CW tools project if exists
        if len(cw_tool_projects) > 0:
            cw_tool_project = cw_tool_projects[0]
            cw_tool_project.set_param_values({"Start Date": datetime_to_wf_format(self.deploy_datetime)})

        # Update "StartDateTimeInclusiveUTC" in TBM project if exists
        if len(tarjeted_bonus_media_projects) > 0:
            tarjeted_bonus_media_project = tarjeted_bonus_media_projects[0]
            tarjeted_bonus_media_project.set_param_values(
                {"StartDateTimeInclusiveUTC": datetime_to_wf_format(self.deploy_datetime)})

        return wf_project

    def build(self):
        '''
        @summary: According to all the parameters set to the builder, build a
        workfront update project.
        @raise WFBrigeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        '''
        self._check_viability()

        # Call the corresponding method to create the update project
        return self.supported_project_types[self.project_type]()
