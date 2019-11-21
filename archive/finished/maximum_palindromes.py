#!/bin/python3
import os
import math

from collections import defaultdict

def initialize(s):
    pass

def compute_dicts(s):
    evenmap = defaultdict(lambda : 0)
    oddset  = set()
    for c in s:
        if c in oddset:
            oddset.remove(c)
            evenmap[c] += 1
        else:
            oddset.add(c)
    return evenmap, oddset

def combinations(n, r):
    factorial = math.factorial
    return int(factorial(n) / (factorial(r) * factorial(n - r)))

def answerQuery(s, l, r):
    s = (s[l-1:r])
    evenmap, oddset = compute_dicts(s)

    o = len(oddset)
    p = sum(v for v in evenmap.values())
    r = len(evenmap)

    x = 1
    for count in evenmap.values():
        x *= math.factorial(count)
    return int(max(1, o) * math.factorial(p) / (x)) % (10 ** 9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(s, l, r)

        fptr.write(str(result) + '\n')

    fptr.close()

