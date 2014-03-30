#!/usr/bin/env python3

# Problem 7: 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
# can see that the 6th prime is 13.

# What is the 10 001st prime number?

from problem3 import primes

def problem7():
    return list(primes(104743))[10000]

if __name__ == '__main__':
    print(problem7())
