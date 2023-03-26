import unittest
import main

class TestMain(unittest.TestCase):

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
    
    def test_do_stuff_string(self):
        test_param = 'akjhasd'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    
    def test_do_stuff_set(self):
        test_param = {1, 2, 3}
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, TypeError)

    def test_do_stuff_float(self):
        test_param = 1.23
        result = main.do_stuff(test_param)
        self.assertEqual(result, 6)

    def test_do_stuff_neg(self):
        test_param = -5
        result = main.do_stuff(test_param)
        self.assertEqual(result, 0)

    def test_do_stuff_string_num(self):
        test_param = '5'
        result = main.do_stuff(test_param)
        self.assertEqual(result, 10)
    
    def test_do_stuff_large(self):
        test_param = 5430829348573456237462834987543123456434234
        result = main.do_stuff(test_param)
        self.assertEqual(result, 5430829348573456237462834987543123456434239)

if __name__ == '__main__':
    unittest.main()
