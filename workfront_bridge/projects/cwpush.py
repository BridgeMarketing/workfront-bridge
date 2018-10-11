from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format
from distutils.util import strtobool


class CWPushContainer(WFBlock):
    """
    @summary: Workfront CW Push Project Container.
    Use this project container to create workfront CW Push projects.
    This project container has no tasks in it but has all the fields of the
    custom forms that a CW Push project needs.
    """

    template_name = "Base Project Container - CW Push"

    def __init__(self, prj_name):
        super(CWPushContainer, self).__init__(self.template_name, name=prj_name)

        req = [
            "Bridge_orderID",
            "Partner Name",
            "Industry",
            "Target Volume",
            "Click Tier",
            "Open Tier",
        ]
        self._add_required_parameters(req)
        opt = [
            "Name",
            "HTML Link",
            "Banner Link",
            "Start Date",
            "Overage",
            "Geo Target",
            "Geo Target State",
            "Deployment File Link",
            "Deployment File Segment",
            "CW Tool Link",
            "Duration"
        ]
        self._add_optional_parameters(opt)

        # Project Container fields:
        self._bridge_order_id = None
        self._order_name = None
        self._partner_name = None
        self._industry = None
        self._html_link = None
        self._banner_link = None
        self._start_date = None
        self._target_volume = None
        self._overage = None
        self._geo_target = None
        self._geo_target_state = None
        self._deployment_file_link = None
        self._deployment_file_segment = None
        self._click_tier = None
        self._open_tier = None
        self._cw_tool_link = None
        self._duration = None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, v):
        self._duration = v
        self.set_parameter("", "Duration", v)

    @property
    def bridge_order_id(self):
        return self._bridge_order_id

    @bridge_order_id.setter
    def bridge_order_id(self, v):
        self._bridge_order_id = v
        self.set_parameter("", "Bridge_orderID", v)

    @property
    def order_name(self):
        return self._order_name

    @order_name.setter
    def order_name(self, v):
        self._order_name = v
        self.set_parameter("", "Name", v)

    @property
    def partner_name(self):
        return self._partner_name

    @partner_name.setter
    def partner_name(self, v):
        self._partner_name = v
        self.set_parameter("", "Partner Name", v)

    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, v):
        self._industry = v
        self.set_parameter("", "Industry", v)

    @property
    def html_link(self):
        return self._html_link

    @html_link.setter
    def html_link(self, v):
        self._html_link = v
        self.set_parameter("", "HTML Link", v)

    @property
    def banner_link(self):
        return self._banner_link

    @banner_link.setter
    def banner_link(self, v):
        self._banner_link = v
        self.set_parameter("", "Banner Link", v)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, v):
        self._start_date = v
        self.set_parameter("", "Start Date", datetime_to_wf_format(v))

    @property
    def target_volume(self):
        return self._target_volume

    @target_volume.setter
    def target_volume(self, v):
        self._target_volume = v
        self.set_parameter("", "Target Volume", v)

    @property
    def overage(self):
        # type encapsulation: str to bool
        return bool(strtobool(self._overage))

    @overage.setter
    def overage(self, v):
        # type encapsulation: bool to str
        self._overage = str(v)
        self.set_parameter("", "Overage", self._overage)

    @property
    def geo_target(self):
        return self._geo_target

    @geo_target.setter
    def geo_target(self, v):
        self._geo_target = v
        self.set_parameter("", "Geo Target", v)

    @property
    def geo_target_state(self):
        return self._geo_target_state

    @geo_target_state.setter
    def geo_target_state(self, v):
        self._geo_target_state = v
        self.set_parameter("", "Geo Target State", v)

    @property
    def deployment_file_link(self):
        return self._deployment_file_link

    @deployment_file_link.setter
    def deployment_file_link(self, v):
        self._deployment_file_link = v
        self.set_parameter("", "Deployment File link", v)

    @property
    def deployment_file_segment(self):
        return self._deployment_file_segment

    @deployment_file_segment.setter
    def deployment_file_segment(self, v):
        self._deployment_file_segment = v
        self.set_parameter("", "Deployment File Segment", v)

    @property
    def click_tier(self):
        return self._click_tier

    @click_tier.setter
    def click_tier(self, v):
        self._click_tier = v
        self.set_parameter("", "Click Tier", v)

    @property
    def open_tier(self):
        return self._open_tier

    @open_tier.setter
    def open_tier(self, v):
        self._open_tier = v
        self.set_parameter("", "Open Tier", v)

    @property
    def cw_tool_link(self):
        return self._cw_tool_link

    @cw_tool_link.setter
    def cw_tool_link(self, v):
        self._cw_tool_link = v
        self.set_parameter("", "CW Tool Link", v)
