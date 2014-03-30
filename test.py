#!/usr/bin/env python3

import unittest

class Euler(unittest.TestCase):
    def test_problem92(self):
        from problem92 import problem92
        self.assertEqual(problem92(), 8581146)

if __name__ == '__main__':
    unittest.main()
