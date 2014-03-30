#!/usr/bin/env python3

# Problem 3: Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

def primes(n):
    n += 1
    bitset = [0] * n

    for i in range(2, n):
        if not bitset[i]:
            yield i
            for j in range(2*i, n, i):
                bitset[j] = 1

def factors(g, n):
    for i in g:
        if n % i == 0:
            yield i

def problem3():
    n = 600851475143
    return list(factors(primes(int(sqrt(n))), n))[-1]

if __name__ == '__main__':
    print(problem3())
