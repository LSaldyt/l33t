#!/usr/bin/env python

import numpy as np
from time import time

n       = 100000
example = [(0, 10000, 10), (0, 5000, 5), (300, 301, 1)]


def max_account_value(n, rounds):
    accounts = [0 for i in range(n)]
    for start, end, amount in rounds:
        for i in range(start, end):
            accounts[i] += amount
    return max(accounts)

def max_account_value_numpy(n, rounds):
    accounts = np.repeat(0, n)
    for start, end, amount in rounds:
        accounts[start:end] += np.repeat(amount, end-start)
    return np.max(accounts)

def benchmark(f, n, rounds, iterations=10000):
    start = time()
    for i in range(iterations):
        result = f(n, rounds)
    end = time()
    return result, end - start

def main():
    print(benchmark(max_account_value, n, example))
    print(benchmark(max_account_value_numpy, n, example))

if __name__ == '__main__':
    main()
