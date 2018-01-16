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

    def test_reset_works_properly_in_dice_roller(self):
        roller = dice_roller.DiceRoller()
        roller.successes = 10
        roller.failures = 10
        roller.tens = 15
        roller.reset_dice_roller()
        self.assertEqual(roller.successes, 0)
        self.assertEqual(roller.failures, 0)
        self.assertEqual(roller.tens, 0)
        self.assertEqual(roller.results, [(0, [0])])


if __name__ is '__main__':
    unittest.main()
