import unittest

from cube_conundrum import solve_puzzle, sum_bag_powers

class MyTestCase(unittest.TestCase):

    def test_solve_puzzle(self):
        actual = solve_puzzle("test_input.txt")
        self.assertEqual(actual, 8)
    
    def test_solve_puzzle_2(self):
        actual = solve_puzzle("input.txt")
        self.assertGreater(actual, 2436)

    def test_sum_bag_powers(self):
        actual = sum_bag_powers("test_input.txt")
        self.assertEqual(actual, 2286)

if __name__ == '__main__':
    unittest.main()