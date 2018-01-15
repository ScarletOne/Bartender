import threshold_manipulator
import unittest


class TestThresholdManipulator(unittest.TestCase):

    def test_threshold_is_changed(self):
        manipulator = threshold_manipulator.ThresholdManipulator()
        manipulator.change_success_threshold(['command invoker', 5])
        self.assertTrue(manipulator.new_threshold is 5)

    def test_threshold_is_changed_when_its_a_string(self):
        manipulator = threshold_manipulator.ThresholdManipulator()
        manipulator.change_success_threshold(['command invoker', '5'])
        self.assertTrue(manipulator.new_threshold is 5)

    def test_threshold_is_not_changed_when_above_10(self):
        manipulator = threshold_manipulator.ThresholdManipulator()
        manipulator.change_success_threshold(['command invoker', '11'])
        self.assertTrue(manipulator.new_threshold is 7)

    def test_threshold_is_not_changed_when_below_1(self):
        manipulator = threshold_manipulator.ThresholdManipulator()
        manipulator.change_success_threshold(['command invoker', '0'])
        self.assertTrue(manipulator.new_threshold is 7)

    def test_successful_first_change_failure_at_second(self):
        manipulator = threshold_manipulator.ThresholdManipulator()
        manipulator.change_success_threshold(['command invoker', '6'])
        self.assertTrue(manipulator.new_threshold is 6)
        manipulator.change_success_threshold(['command invoker', '1530'])
        self.assertTrue(manipulator.new_threshold is 6)

    def test_reset_works_properly_in_threshold_manipulator(self):
        manipulator = threshold_manipulator.ThresholdManipulator()
        manipulator.change_success_threshold(['command invoker', '6'])
        self.assertTrue(manipulator.new_threshold is 6)
        manipulator.reset_threshold()
        self.assertTrue(manipulator.new_threshold is 7)


if __name__ is '__main__':
    unittest.main()
