# -*- coding: utf-8 -*-
from main import assignment1, assignment2, assignment3
import unittest

class TestCase(unittest.TestCase):

    def test_assignment1(self):
        self.assertEqual(assignment1([0, 1, 2, 5], 1), 1)
        self.assertEqual(assignment1([30, 19, 2, 95], 0), 30)
        self.assertEqual(assignment1([450, 97919, 29876, 96153, 9853475, 2458], 4), 9853475)

    def test_assignment2(self):
        self.assertEqual(assignment2({0:1, 2:0, 1:2}, 0), 1)
        self.assertEqual(assignment2({0:1, 2:0, 1:2}, 1), 2)
        self.assertEqual(assignment2({0:1, 2:0, 1:2}, 2), 0)

    def test_assignment3(self):
        self.assertEqual(assignment3([0, 1, 2], 3), [0, 1, 2, 3])
        self.assertEqual(assignment3([0, 1, 2, 5, 1], 56), [0, 1, 2, 5, 1, 56])
        self.assertEqual(assignment3(['0', '1', '2', '5', '1'], '56'),
                         ['0', '1', '2', '5', '1', '56'])

if __name__ == "__main__":
    unittest.main()
