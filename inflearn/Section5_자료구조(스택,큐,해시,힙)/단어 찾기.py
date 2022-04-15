from collections import Counter, defaultdict


def solution():

    n = int(input())

    d = defaultdict(int)

    for _ in range(n + n - 1):
        word = input()
        d[word] += 1

    counter = Counter(d)

    return counter.most_common()[-1][0]


print(solution())