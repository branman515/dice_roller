import unittest
import mock
import builtins
import DiceRoll.dice_roller as DiceRoller

class Testing(unittest.TestCase):
    def test_input_dice_1(self):
        test_dice = DiceRoller.Dice_roller()
        with mock.patch.object(builtins, 'input', lambda _: '1'):
            assert test_dice.num_die() == 1
    
    def test_input_dice_2(self):
        test_dice = DiceRoller.Dice_roller()
        with mock.patch.object(builtins, 'input', lambda _: '2'):
            assert test_dice.num_die() == 2


if __name__ == '__main__':
    unittest.main()