#!/usr/bin/env python

import numpy as np
from time import time

EXAMPLES = [(1000, [(i, i + 1, 1) for i in range(999)])]
EXAMPLES = [(10000, [(i, i + 100, 1) for i in range(100)])]

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

def max_account_value_sparse(n, rounds):
    accounts = [(0, n, 0)]
    for start, end, amount in rounds:
        new_accounts = []
        for a_start, a_end, a_amount in accounts:
            # No overlap
            if start >= a_end or end < a_start:
                new_accounts.append((a_start, a_end, a_amount))
                continue
            # Left gap
            if start > a_start:
                new_accounts.append((a_start, start, a_amount))
                overlap_start = start
            else:
                overlap_start = a_start

            # Right gap
            if end < a_end:
                overlap_end = end
            else:
                overlap_end = a_end

            # Middle
            new_accounts.append((overlap_start, overlap_end, a_amount + amount))

            # Add right gap later to maintain sorted
            if end < a_end:
                new_accounts.append((end, a_end, a_amount))
        accounts = new_accounts

    return max(account[2] for account in accounts)

def benchmark(f, n, rounds, iterations=1000, name=''):
    start = time()
    for i in range(iterations):
        result = f(n, rounds)
    end = time()
    print(name, ':')
    print(result, end - start)

def main():
    iterations = 1000
    for i, (n, example) in enumerate(EXAMPLES):
        print('Example ', i)
        benchmark(max_account_value,        n, example, name='Normal', iterations=iterations)
        benchmark(max_account_value_numpy,  n, example, name='Numpy', iterations=iterations)
        benchmark(max_account_value_sparse, n, example, name='Sparse', iterations=iterations)

if __name__ == '__main__':
    main()
