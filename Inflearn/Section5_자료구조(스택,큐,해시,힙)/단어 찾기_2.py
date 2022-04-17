from collections import defaultdict


def solution():

    n = int(input())

    d = defaultdict(int)

    for _ in range(n + n - 1):
        word = input()
        d[word] += 1

    for k, v in d.items():
        if v == 1:
            return k


print(solution())