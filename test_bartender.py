import unittest
from source.unit_tests import test_dice_roller,\
    test_threshold_manipulator


def main():
    unittest.main()


if __name__ is '__main__':
    unittest.TextTestRunner(verbosity=2).run(test_dice_roller.all_tests)
    unittest.TextTestRunner(verbosity=2).run(test_threshold_manipulator.all_tests)
