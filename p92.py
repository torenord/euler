#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from functools import lru_cache
from multiprocessing import Pool, cpu_count

def f(n):
    res = 0
    while n:
        m = n % 10
        n = n // 10
        res += m * m
    return res

def g1(n):
    return n if n == 1 or n == 89 else g2(f(n))

@lru_cache(maxsize=None)
def g2(n):
    return n if n == 1 or n == 89 else g2(f(n))

def h(n):
    p = Pool(cpu_count())
    lst = p.map(g1, range(1, n))
    return len([1 for i in lst if i == 89])

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
    except:
        print('Usage: %s n' % (sys.argv[0]))
        sys.exit(1)

    print(h(n))
