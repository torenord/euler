#!/usr/bin/env python3

# Problem 5: Smallest multiple

# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

from functools import reduce

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

def problem5():
    return reduce(lcm, range(1, 20))

if __name__ == '__main__':
    print(problem5())
