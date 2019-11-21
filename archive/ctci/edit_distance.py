#!/usr/bin/env python3

def check_distance(a, b):
    diff = abs(len(a) - len(b))
    if diff > 1:
        return False

    boff = 0
    aoff = 0
    edits = 0

    end = min(len(a) , len(b))
    for i in range(max(len(a), len(b))):
        if i < end:
            if a[i + aoff] == b[i + boff]:
                continue
            else:
                if diff != 0:
                    if len(a) > len(b):
                        aoff = 1
                    else:
                        boff = 1
                edits += 1
                if edits > 1:
                    return False
    return True

def main():
    test_cases = [('rice', 'ice'),
                  ('rice', 'rices'),
                  ('', 'a'),
                  ('a', ''),
                  ('rice', 'race'),
                  ('rice', 'wheat')]
    for a, b in test_cases:
        print('Checking {} versus {} : {}'.format(a, b, check_distance(a, b)))

main()
