import unittest

from trebuchet import find_calibration_sum


class TrebuchetTestCase(unittest.TestCase):

    def test_sum_calibration_values(self):
        actual = find_calibration_sum("test_input.txt")
        self.assertEqual(actual, 142)
        
    def test_sum_calibration_values_with_letters(self):
        actual = find_calibration_sum("test_input_2.txt")
        self.assertEqual(actual, 281)
        
    def test_sum_calibration_values_actual(self):
        actual = find_calibration_sum("input.txt")
        self.assertGreater(actual, 54086)


if __name__ == '__main__':
    unittest.main()
