#!/usr/bin/env python3

# Problem 22: Names scores

# Using names.txt (right click and 'Save Link/Target As...'), a 46K
# text file containing over five-thousand first names, begin by
# sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
# list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

with open('names.txt') as f:
    names = f.read().replace('\"', '').split(',')

def alphabeticalvalue(name):
    return sum([ord(l)-ord('A')+1 for l in name])

def problem22():
    S = 0
    i = 1

    for name in sorted(names):
        S += i * alphabeticalvalue(name)
        i += 1

    return S

if __name__ == '__main__':
    print(problem22())
