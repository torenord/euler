#!/usr/bin/env python3

# Problem 20: Factorial digit sum

# n! means n x (n − 1) x ... x 3 x 2 x 1

# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum
# of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def factorial(n):
    if n < 1: return 1
    else: return n * factorial(n-1)

def problem20():
    return sum([int(d) for d in str(factorial(100))])

if __name__ == '__main__':
    print(problem20())
