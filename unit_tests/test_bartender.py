import unittest
import test_dice_roller


def main():
    unittest.main()


if __name__ is '__main__':
    unittest.TextTestRunner(verbosity=2).run(test_dice_roller.all_tests)
