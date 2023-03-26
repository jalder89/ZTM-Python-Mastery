# Testing for the random game systems
import unittest
import system.game

class TestRandomGame(unittest.TestCase):

    def test_random(self):
        lower_num = 1
        upper_num = 10
        count = 50

        while count > 0:
            result = system.game.get_random(lower_num, upper_num)
            self.assertGreaterEqual(result, lower_num)
            self.assertLessEqual(result, upper_num)
            count -= 1
    
    def test_random_string(self):
        lower_num = 1
        upper_num = 10
        result = system.game.get_random('a', upper_num)
        self.assertIsInstance(result, ValueError)

    def test_guess(self):
        lower_num = 1
        upper_num = 10
        number = system.game.get_random(lower_num, upper_num)
        count = 10

        while count > 0:
            result = system.game.check_guess(count, number)
            self.assertIsInstance(result, bool)
            count -= 1
    
    def test_guess_string(self):
        lower_num = 1
        upper_num = 10
        number = system.game.get_random(lower_num, upper_num)
        result = system.game.check_guess('a', number)
        self.assertIsInstance(result, ValueError)


if __name__ == '__main__':
    unittest.main()