#!/usr/bin/env python3

# Problem 17: Number letter counts

# If the numbers 1 to 5 are written out in words: one, two, three,
# four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
# total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three
# hundred and forty-two) contains 23 letters and 115 (one hundred and
# fifteen) contains 20 letters. The use of "and" when writing out
# numbers is in compliance with British usage.

def tocardinal(n):
    if n == 0:
        return ""

    cardinalnumbers = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    if n in cardinalnumbers:
        return cardinalnumbers[n]

    if n < 100:
        return tocardinal(n // 10 * 10) + "-" + tocardinal(n % 10)

    if n < 1000:
        s = " and " + tocardinal(n % 100) if tocardinal(n % 100) != "" else ""
        return tocardinal(n // 100) + " hundred" + s

    if n < 10000:
        return tocardinal(n // 1000) + " thousand"

def problem17():
    N = 1000

    count = 0
    for cardinal in [tocardinal(i) for i in range(1, N+1)]:
        count += len(cardinal.replace(" ", "").replace("-", ""))

    return count

if __name__ == '__main__':
    print(problem17())
