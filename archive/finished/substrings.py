#!/bin/python3

import os
import sys

from pprint import pprint

#
# Complete the countSubstrings function below.
#
def countSubstrings(s, queries):
    q = []
    for a, b in queries:
        seen = set()
        sub = s[a:b+1]
        seen.add(sub)
        #print(sub)
        for i in range(len(sub)):
            for j in range(i+1, len(sub)+1):
                subsub = sub[i:j]
                seen.add(subsub)
        #print('*' * 90)
        #pprint(seen)
        q.append(len(seen))
    return q

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    s = input()

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = countSubstrings(s, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

