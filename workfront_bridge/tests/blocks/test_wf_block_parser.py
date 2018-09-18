import unittest

from workfront_bridge.blocks.base import WFBlockParser, WFBlock


class WFBlockParserTestCase(unittest.TestCase):

    def test_contructor(self):
        wf = None
        obj = WFBlockParser(wf)

    def test_get_project_temporal_name(self):
        wf = None
        obj = WFBlockParser(wf)

        temporal_project_name = obj._get_temporal_project_name()
        self.assertIn("Temporary Block Generic - ", temporal_project_name)

        temporal_project_name = obj._get_temporal_project_name("prefix1111")
        self.assertIn("Temporary Block prefix1111 - ", temporal_project_name)

    def test_create(self):
        wf = None

        project = WFBlock("project_template_1", "test project creation")
        obj = WFBlockParser(wf)

        #obj.create(project)
