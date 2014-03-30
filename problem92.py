#!/usr/bin/env python3

# Problem 92: Square digit chains

# A number chain is created by continuously adding the square of the
# digits in a number to form a new number until it has been seen
# before.

# For example,

# 44 -> 32 -> 13 -> 10 -> 1 -> 1
# 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an
# endless loop. What is most amazing is that EVERY starting number
# will eventually arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?

from functools import lru_cache
from multiprocessing import Pool, cpu_count

def f(n):
    res = 0
    while n:
        m = n % 10
        n = n // 10
        res += m * m
    return res

def g0(n):
    return g(f(n))

@lru_cache(maxsize=None)
def g(n):
    return n == 89 if n == 1 or n == 89 else g(f(n))

def problem92():
    p = Pool(cpu_count())
    return sum(p.map(g0, range(1, 10000000)))

if __name__ == '__main__':
    print(problem92())
