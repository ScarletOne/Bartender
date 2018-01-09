import dice_roller
import roll_parameters
import unittest


class TestDiceRoller(unittest.TestCase):

    def test_good_default_threshold_taken(self):
        roll_parameters.roll_parameters['success_threshold'] = 7
        roller = dice_roller.DiceRoller()
        self.assertEqual(roller.success_threshold, 7)

    def test_changing_threshold_affects_successes(self):
        roll_parameters.roll_parameters['success_threshold'] = 5
        roller = dice_roller.DiceRoller()
        self.assertEqual(roller.success_threshold, 5)


all_tests = unittest.TestSuite()
all_tests.addTest(TestDiceRoller('test_good_default_threshold_taken'))
all_tests.addTest(TestDiceRoller('test_changing_threshold_affects_successes'))
