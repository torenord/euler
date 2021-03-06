#!/usr/bin/env python3

# Problem 15: Lattice paths

# Starting in the top left corner of a 2×2 grid, and only being able
# to move to the right and down, there are exactly 6 routes to the
# bottom right corner.

# How many such routes are there through a 20×20 grid?

def countroutes(n):
    result = 1

    for i in range(1, n+1):
        result = result * (n + i)//i

    return result

def problem15():
    return countroutes(20)

if __name__ == '__main__':
    print(problem15())
