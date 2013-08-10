#!/usr/bin/env python3

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

def h(n):
    p = Pool(cpu_count())
    return sum(p.map(g0, range(1, n)))

if __name__ == '__main__':
    import sys

    try:
        n = int(sys.argv[1])
    except:
        print('Usage: %s n' % (sys.argv[0]))
        sys.exit(1)

    print(h(n))
