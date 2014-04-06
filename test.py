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

    def test_problem11(self):
        from problem11 import problem11
        self.assertEqual(problem11(), 70600674)

    def test_problem12(self):
        from problem12 import problem12
        self.assertEqual(problem12(), 76576500)

    def test_problem13(self):
        from problem13 import problem13
        self.assertEqual(problem13(), 5537376230)

    def test_problem14(self):
        from problem14 import problem14
        self.assertEqual(problem14(), 837799)

    def test_problem18(self):
        from problem18 import problem18
        self.assertEqual(problem18(), 1074)

    def test_problem21(self):
        from problem21 import problem21
        self.assertEqual(problem21(), 31626)

    def test_problem25(self):
        from problem25 import problem25
        self.assertEqual(problem25(), 4782)

    def test_problem67(self):
        from problem67 import problem67
        self.assertEqual(problem67(), 7273)

    def test_problem92(self):
        from problem92 import problem92
        self.assertEqual(problem92(), 8581146)

if __name__ == '__main__':
    unittest.main()
