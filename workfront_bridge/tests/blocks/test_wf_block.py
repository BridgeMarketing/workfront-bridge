import unittest

from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.exceptions import WFBrigeException


class WFBlockTestCase(unittest.TestCase):

    def test_contructor(self):
        template_id = "temp1234"
        obj = WFBlock(template_id, name="block name")

        self.assertEqual(template_id, obj.wf_template_name)
        self.assertEqual("block name", obj.name)

    def test_members_default_values(self):
        obj = WFBlock("1234")

        self.assertEqual([], obj.blocks)
        self.assertEqual({}, obj.parameters)
        self.assertEqual([], obj.required_parameters)
        self.assertEqual([], obj.optional_parameters)
        self.assertEqual(1, obj.starter_task_identifier)

    def test_append(self):
        obj = WFBlock("1234")
        child_block1 = WFBlock("child_block")
        child_block2 = WFBlock("child_block2")

        obj.append(child_block1)
        obj.append(child_block2)

        self.assertEqual([child_block1, child_block2], obj.blocks)

    def test_set_parameter(self):
        obj = WFBlock("1234")

        obj.set_parameter("task Name 1", "customField1", "customField1Value")
        self.assertEqual(obj.parameters, {"task Name 1": {"customField1": "customField1Value"}})

        obj.set_parameter("task Name 2", "customField2", "customField2Value")
        self.assertEqual(obj.parameters, {
            "task Name 1": {"customField1": "customField1Value"},
            "task Name 2": {"customField2": "customField2Value"}
        })

        obj.set_parameter("task Name 1", "customField1_2", "customField1_2Value")
        self.assertEqual(obj.parameters, {
            "task Name 1": {"customField1": "customField1Value", "customField1_2": "customField1_2Value"},
            "task Name 2": {"customField2": "customField2Value"}
        })

    def test_set_required_parameters(self):
        obj = WFBlock("1234")

        obj._add_required_parameters(["required1", "required2"])
        self.assertEqual(obj.required_parameters, ["required1", "required2"])

        obj._add_required_parameters(["required3", "required4"])
        self.assertEqual(obj.required_parameters, ["required1", "required2", "required3", "required4"])

    def test_set_optional_parameters(self):
        obj = WFBlock("1234")

        obj._add_optional_parameters(["optionalfield1", "optionalfield2"])
        self.assertEqual(obj.optional_parameters, ["optionalfield1", "optionalfield2"])

        obj._add_optional_parameters(["optionalfield3", "optionalfield4"])
        self.assertEqual(obj.optional_parameters, ["optionalfield1", "optionalfield2", "optionalfield3", "optionalfield4"])

    def test_check_parameters(self):
        obj = WFBlock("1234")

        obj._add_required_parameters(["requiredfield1", "requiredfield2"])
        obj._add_optional_parameters(["optionalfield1", "optionalfield2"])
        self.assertRaises(WFBrigeException, obj.check_parameters)

        obj.set_parameter("Task 1", "requiredfield1", "a")
        obj.set_parameter("Task 2", "requiredfield2", "b")
        obj.set_parameter("Task 1", "optionalfield1", "c")
        obj.set_parameter("Task 1", "optionalfield2", "d")
        try:
            obj.check_parameters()
        except WFBrigeException:
            self.fail("_check_param_values() raised WFBrigeException")

        obj.set_parameter("Task 1", "Non_exist_optionalfield", "x")
        self.assertRaises(WFBrigeException, obj.check_parameters)

    def _set_starter_task(self):
        obj = WFBlock("1234")

        obj._set_starter_task(12)

        self.assertEqual(12, obj.starter_task_identifier)
