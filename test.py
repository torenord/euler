#!/usr/bin/env python3

import unittest

class Euler(unittest.TestCase):
    def test_problem1(self):
        from problem1 import problem1
        self.assertEqual(problem1(), 233168)

    def test_problem2(self):
        from problem2 import problem2
        self.assertEqual(problem2(), 4613732)

    def test_problem3(self):
        from problem3 import problem3
        self.assertEqual(problem3(), 6857)

    def test_problem4(self):
        from problem4 import problem4
        self.assertEqual(problem4(), 906609)

    def test_problem5(self):
        from problem5 import problem5
        self.assertEqual(problem5(), 232792560)

    def test_problem6(self):
        from problem6 import problem6
        self.assertEqual(problem6(), 25164150)

    def test_problem7(self):
        from problem7 import problem7
        self.assertEqual(problem7(), 104743)

    def test_problem8(self):
        from problem8 import problem8
        self.assertEqual(problem8(), 40824)

    def test_problem9(self):
        from problem9 import problem9
        self.assertEqual(problem9(), 31875000)

    def test_problem10(self):
        from problem10 import problem10
        self.assertEqual(problem10(), 142913828922)

    def test_problem92(self):
        from problem92 import problem92
        self.assertEqual(problem92(), 8581146)

if __name__ == '__main__':
    unittest.main()