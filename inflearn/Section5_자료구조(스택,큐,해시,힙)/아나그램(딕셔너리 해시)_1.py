from collections import defaultdict


def solution():

    d = defaultdict(int)

    for c in input():
        d[c] += 1

    for c in input():
        d[c] -= 1

    for k, v in d.items():
        if v != 0:
            return 'NO'

    return 'YES'


print(solution())





