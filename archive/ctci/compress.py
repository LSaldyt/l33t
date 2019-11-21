#!/usr/bin/env python3

def compress(s):
    reduced = []
    for c in s:
        if reduced and reduced[-1][0] == c:
            reduced[-1] = (c, reduced[-1][1] + 1)
        else:
            reduced.append((c, 1))
    if sum(1 + x // 10 for _, x in reduced) < len(s):
        return ''.join(c + str(x) for c, x in reduced)
    else:
        return s

def main():
    test_cases = ['aaabbbddd', 'abd']
    for case in test_cases:
        print('{} -> {}'.format(case, compress(case)))

main()
