import unittest

from workfront_bridge.blocks.base import WFBlock, WFProjectContainer
from workfront_bridge.exceptions import WFBrigeException


class WFProjectContainerTestCase(unittest.TestCase):

    def test_contructor(self):
        wf = None
        template_id = "temp456"
        project_name = "project name"
        obj = WFProjectContainer(wf, template_id, project_name)
        self.assertEqual(template_id, obj.wf_template_id)
        self.assertEqual(project_name, obj.prj_name)

    def test_members_default_values(self):
        wf = None
        obj = WFProjectContainer(wf, "1", "pn")
        self.assertEqual([], obj.blocks)
        self.assertEqual({}, obj.param_values)
        self.assertEqual([], obj.req_fields)
        self.assertEqual([], obj.opt_fields)

    def test_append(self):
        wf = None
        obj = WFProjectContainer(wf, "1", "pn")

        new_block = WFBlock(wf, "template1234")
        obj.append(new_block)
        self.assertEqual(obj.blocks, [new_block])

        new_block2 = WFBlock(wf, "templateABC")
        obj.append(new_block2)
        self.assertEqual(obj.blocks, [new_block, new_block2])

    def test_set_param_value(self):
        wf = None
        obj = WFProjectContainer(wf, "1", "pn")
        obj.set_param_value("field1", "value1")
        obj.set_param_value("field2", "value2")

        self.assertEqual(obj.param_values, {"field1": "value1", "field2": "value2"})

    def test_set_required_fields(self):
        wf = None
        obj = WFProjectContainer(wf, "1", "pn")

        obj._set_required_fields(["requiredfield1", "requiredfield2"])
        self.assertEqual(obj.req_fields, ["requiredfield1", "requiredfield2"])

        obj._set_required_fields(["requiredfield3", "requiredfield4"])
        self.assertEqual(obj.req_fields, ["requiredfield1", "requiredfield2", "requiredfield3", "requiredfield4"])

    def test_set_optional_fields(self):
        wf = None
        obj = WFProjectContainer(wf, "1", "pn")

        obj._set_optional_fields(["optionalfield1", "optionalfield2"])
        self.assertEqual(obj.opt_fields, ["optionalfield1", "optionalfield2"])

        obj._set_optional_fields(["optionalfield3", "optionalfield4"])
        self.assertEqual(obj.opt_fields, ["optionalfield1", "optionalfield2", "optionalfield3", "optionalfield4"])

    def test_check_param_values(self):
        wf = None
        obj = WFProjectContainer(wf, "1", "pn")

        obj._set_required_fields(["requiredfield1", "requiredfield2"])
        obj._set_optional_fields(["optionalfield1", "optionalfield2"])
        self.assertRaises(WFBrigeException, obj._check_param_values)

        obj.set_param_value("requiredfield1", "a")
        obj.set_param_value("requiredfield2", "b")
        obj.set_param_value("optionalfield1", "c")
        obj.set_param_value("optionalfield2", "d")
        try:
            obj._check_param_values()
        except WFBrigeException:
            self.fail("_check_param_values() raised WFBrigeException")

        obj.set_param_value("Non_exist_optionalfield", "x")
        self.assertRaises(WFBrigeException, obj._check_param_values)

    def test_create(self):
        pass
