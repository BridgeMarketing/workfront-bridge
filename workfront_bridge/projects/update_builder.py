import json
from datetime import datetime, date

from workfront.objects.project import WFProject

from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.projects.update import WFProjectUpdateContainer

from workfront_bridge.blocks.update import WFUpdateEmailDeployBlock, WFUpdateMediaDeployBlock
from workfront_bridge.tools import datetime_to_wf_format
from workfront_bridge.util.jsonutil import DateTimeEncoder


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
            "Display - Desktop": self.__build_update_media_deploy,
            "Display - Mobile": self.__build_update_media_deploy,
            "Display - Desktop & Mobile": self.__build_update_media_deploy,
            "BridgeConnect - Desktop": self.__build_update_media_deploy,
            "BridgeConnect - Mobile": self.__build_update_media_deploy,
            "BridgeConnect - Desktop & Mobile": self.__build_update_media_deploy,
            "Audio": self.__build_update_media_deploy,
            "Video": self.__build_update_media_deploy,
        }
        self.wf = wf

        self.wf_project_id = None
        self.deploy_datetime = None
        self.project_type = None  # Project type being updated
        self.start_datetime = None
        self.end_datetime = None

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

    def set_new_start_datetime(self, start_datetime):
        '''
        @param start_datetime: from datetime to update
        '''
        self.start_datetime = start_datetime
        return self

    def set_new_end_datetime(self, end_datetime):
        '''
        @param end_datetime: to datetime to update
        '''
        self.end_datetime = end_datetime
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
        self.__fullfill_project_type()
        check_not_none("project_type", self.project_type)

        if self.project_type == "Email":
            check_not_none("deploy_datetime", self.deploy_datetime)
        else:
            check_not_none("start_datetime", self.start_datetime)
            check_not_none("end_datetime", self.end_datetime)

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

        targeted_bonus_media_projects = [p for p in all_project if p.name.startswith("TBM - ")]

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
        if len(targeted_bonus_media_projects) > 0:
            tarjeted_bonus_media_project = targeted_bonus_media_projects[0]
            tarjeted_bonus_media_project.set_param_values(
                {"StartDateTimeInclusiveUTC": datetime_to_wf_format(self.deploy_datetime)})

        return wf_project

    def __build_update_media_deploy(self):
        """
        @return: wf project to update a media project.
        """

        prj_being_updated = WFProject(self.wf, self.wf_project_id)
        original_tasks = prj_being_updated.get_tasks()

        prj_name = "Update - {}".format(prj_being_updated.name)
        project = WFProjectUpdateContainer(prj_name)
        update_block = WFUpdateMediaDeployBlock()
        update_block.data = json.dumps(
            {
                "to_update_wf_project_id": self.wf_project_id,
                "start_datetime": self.start_datetime,
                "end_datetime": self.end_datetime,
            },
            cls=DateTimeEncoder,
        )

        project.append(update_block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        tasks = prj_being_updated.get_tasks()
        last_original_task_idx = len(original_tasks) - 1
        update_task = wf_project.get_tasks()[0]
        update_task.add_predecessor(tasks[last_original_task_idx])
        return wf_project

    def build(self):
        """
        @summary: According to all the parameters set to the builder, build a
        workfront update project.
        @raise WFBrigeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        """
        self._check_viability()

        # Call the corresponding method to create the update project
        return self.supported_project_types[self.project_type]()


