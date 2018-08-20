import unittest

from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.exceptions import WFBrigeException


class WFBlockTestCase(unittest.TestCase):

    def test_contructor(self):
        template_id = "temp1234"
        wf = None
        obj = WFBlock(wf, template_id)
        self.assertEqual(template_id, obj.wf_template_id)

    def test_members_default_values(self):
        wf = None
        obj = WFBlock(wf, "1234")
        self.assertEqual({}, obj.task_params)
        self.assertEqual([], obj.req_fields)
        self.assertEqual([], obj.opt_fields)
        self.assertEqual(1, obj.starter_task_identifier)

    def test_set_task_param_value(self):
        wf = None
        obj = WFBlock(wf, "1234")

        obj.set_task_param_value("task Name 1", "customField1", "customField1Value")
        self.assertEqual(obj.task_params, {"task Name 1": {"customField1": "customField1Value"}})

        obj.set_task_param_value("task Name 2", "customField2", "customField2Value")
        self.assertEqual(obj.task_params, {
            "task Name 1": {"customField1": "customField1Value"},
            "task Name 2": {"customField2": "customField2Value"}
        })

        obj.set_task_param_value("task Name 1", "customField1_2", "customField1_2Value")
        self.assertEqual(obj.task_params, {
            "task Name 1": {"customField1": "customField1Value", "customField1_2": "customField1_2Value"},
            "task Name 2": {"customField2": "customField2Value"}
        })

    def test_set_required_fields(self):
        wf = None
        obj = WFBlock(wf, "1234")

        obj._set_required_fields(["requiredfield1", "requiredfield2"])
        self.assertEqual(obj.req_fields, ["requiredfield1", "requiredfield2"])

        obj._set_required_fields(["requiredfield3", "requiredfield4"])
        self.assertEqual(obj.req_fields, ["requiredfield1", "requiredfield2", "requiredfield3", "requiredfield4"])

    def test_set_optional_fields(self):
        wf = None
        obj = WFBlock(wf, "1234")

        obj._set_optional_fields(["optionalfield1", "optionalfield2"])
        self.assertEqual(obj.opt_fields, ["optionalfield1", "optionalfield2"])

        obj._set_optional_fields(["optionalfield3", "optionalfield4"])
        self.assertEqual(obj.opt_fields, ["optionalfield1", "optionalfield2", "optionalfield3", "optionalfield4"])

    def test_check_param_values(self):
        wf = None
        obj = WFBlock(wf, "1234")

        obj._set_required_fields(["requiredfield1", "requiredfield2"])
        obj._set_optional_fields(["optionalfield1", "optionalfield2"])
        self.assertRaises(WFBrigeException, obj._check_param_values)

        obj.set_task_param_value("Task 1", "requiredfield1", "a")
        obj.set_task_param_value("Task 2", "requiredfield2", "b")
        obj.set_task_param_value("Task 1", "optionalfield1", "c")
        obj.set_task_param_value("Task 1", "optionalfield2", "d")
        try:
            obj._check_param_values()
        except WFBrigeException:
            self.fail("_check_param_values() raised WFBrigeException")

        obj.set_task_param_value("Task 1", "Non_exist_optionalfield", "x")
        self.assertRaises(WFBrigeException, obj._check_param_values)

    def test_attach_to_project(self):
        pass
