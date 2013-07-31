#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def f(n):
    return sum(map(lambda x: int(x)*int(x), list(str(n))))

@lru_cache(maxsize=None)
def g(n):
    if n == 1 or n == 89:
        return n
    else:
        return g(f(n))

def h(n):
    return sum([1 for i in range(1, n) if g(i) == 89])

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
    except:
        print('Usage: %s n' % (sys.argv[0]))
        sys.exit(1)

    print(h(n))
