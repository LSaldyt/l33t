#!/bin/python3

# https://www.hackerrank.com/challenges/circular-palindromes/problem

import os
import sys

#
# Complete the circularPalindromes function below.
#
def circularPalindromes(s):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = circularPalindromes(s)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

