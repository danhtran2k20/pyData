# from unittest import TestCase
import unittest

from prob22_linear_algebra import solution

# class Test(TestCase):
class UnitTests(unittest.TestCase):
    
    def test_solution(self):
        # provided test-cases
        self.assertEqual([12, 1], solution([4, 30, 50]))
        self.assertEqual([-1, -1], solution([4, 17, 50]))

        # my own test-cases
        self.assertEqual([10, 3], solution([5, 10]))

        # test-cases from Stack Overflow @thiswind
        self.assertEqual([100, 3], solution([1, 51]))
        self.assertEqual([20, 1], solution([1, 31]))
        self.assertEqual([20, 1], solution([1, 31, 51, 71]))
        self.assertEqual([20, 1], solution([1, 31, 51, 71, 91]))
        self.assertEqual([4, 1], solution([4, 9, 17, 31, 40]))

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")