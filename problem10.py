#!/usr/bin/env python3

# Problem 10: Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from problem3 import primes

def problem10():
    return sum(primes(2000000))

if __name__ == '__main__':
    print(problem10())
