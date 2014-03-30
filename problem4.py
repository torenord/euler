#!/usr/bin/env python3

# Problem 4: Largest palindrome product

# A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers is 9009 = 91
# x 99.

# Find the largest palindrome made from the product of two 3-digit
# numbers.

def productsof3digitfactors():
    for i in range(100, 1000):
        for j in range(i, 1000):
            yield i * j

def palindromes(g):
    for i in g:
        s = str(i)
        if s == s[::-1]:
            yield i

def problem4():
    return max(palindromes(productsof3digitfactors()))

if __name__ == '__main__':
    print(problem4())
