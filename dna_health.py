#!/bin/python3
# https://www.hackerrank.com/challenges/determining-dna-health/problem

import math
import os
import random
import re
import sys

def compute_lookups(first, last, genes, healths):
    root_lookup = {}
    lookup = root_lookup
    for i in range(first, last+1):
        gene = genes[i]
        health = healths[i]
        for j, char in enumerate(gene):
            if char in lookup:
                subd, s = lookup[char]
                if j == len(gene) - 1:
                    lookup[char] = subd, s + health
            else:
                subd = {}
                lookup[char] = (subd, health if j == len(gene) - 1 else 0)
            lookup = subd
        lookup = root_lookup
    return root_lookup

def score(d, i, lookup):
    total = 0
    while i < len(d):
        c = d[i]
        j = i
        subd = lookup
        while c in subd:
            subd, s = subd[c]
            total += s
            j += 1
            if j < len(d):
                c = d[j]
            else:
                break
        i += 1
    return total

def print_extreme(ss):
    totals = {score(d, 0, compute_lookups(first, last, genes, health)) for first, last, d in ss}
    print('{} {}'.format(min(totals), max(totals)))

if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input())

    ss = []

    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]
        ss.append((first, last, d))
    print_extreme(ss)

