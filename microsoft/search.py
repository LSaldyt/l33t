# Lucas Saldyt 2019
import sys
import time

def main(args):
    problem = ['abcd', '1234', 'efgd', '567c']
    queries = ['ab2', 'efg', '1234dc']
    problem = ['aaaaa'] * 5
    queries = ['a' * 7]
    print('Problem:')
    for row in problem:
        print(row)
    for query in queries:
        begin  = time.time()
        first  = exhaustive(problem, query)
        mid    = time.time()
        second = exhaustive(problem, query, save=True)
        final  = time.time()
        print('Query: {} Occurances: {} Time: {}'.format(query, first, mid - begin))
        print('Query: {} Occurances: {} Time: {}'.format(query, second, final - mid))
    return 0


def exhaustive(array, query, save=False):
    '''
    Count the number of occurances of query in array
    '''
    cache = dict()
    if len(array) == 0 or len(query) == 0:
        return 0
    x, y = len(array), len(array[0])
    total = 0
    for i in range(x):
        for j in range(y):
            if array[i][j] == query[0]:
                seen = set()
                seen.add((i, j))
                total += count(array, seen, query[1:], i, j, x, y, cache, save)
                seen.remove((i, j))
    return total

def valid(i, j, x, y):
    return i > -1 and j > -1 and i < x and j < y

def count(array, seen, query, i, j, x, y, cache, save):
    if len(query) == 0:
        return 1
    if save and (tuple(sorted(list(seen))), query, i, j) in cache:
        return cache[(tuple(sorted(list(seen))), query, i, j)]
    neighbors = [(i, j) for(i, j) in [(i - 1, j - 1),
                                      (i - 1, j),
                                      (i, j - 1),
                                      (i + 1, j),
                                      (i, j + 1),
                                      (i + 1, j + 1),
                                      (i + 1, j - 1),
                                      (i - 1, j + 1)] if valid(i, j, x, y)]
    total = 0
    for ni, nj in neighbors:
        if (ni, nj) not in seen:
            if array[ni][nj] == query[0]:
                seen.add((ni, nj))
                total += count(array, seen, query[1:], ni, nj, x, y, cache, save)
                seen.remove((ni, nj))
    if save:
        cache[(tuple(sorted(list(seen))), query, i, j)] = total
    return total

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
