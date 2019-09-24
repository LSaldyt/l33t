#!/bin/python3
#https://www.hackerrank.com/challenges/largest-permutation/problem

import math
import os
import random
import re
import sys

def largestPermutation(k, a):
    index = {v : i for i, v in enumerate(a)}
    i = 0
    while i < n and k > 0:
        if (a[i] == n - i):
            i += 1
            continue
        a[index[n - i]] = a[i]
        index[a[i]] = index[n - i]
        a[i] = n - i
        index[n - i] = i
        i += 1
        k -= 1
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

