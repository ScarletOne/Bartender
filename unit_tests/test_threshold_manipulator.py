import threshold_manipulator
import unittest
import discord


class TestThresholdManipulator(unittest.TestCase):

    def test_threshold_is_changed(self):
        manipulator = threshold_manipulator.ThresholdManipulator()
        manipulator.change_success_threshold(['command invoker', 5])
        self.failUnless(manipulator.new_threshold == 5)


all_tests = unittest.TestSuite()
all_tests.addTest(TestThresholdManipulator('test_threshold_is_changed'))