import collections


def solution(clothes):
    d = collections.defaultdict(int)

    for row in clothes:
        kind = row[1]
        d[kind] += 1

    answer = 1
    for value in d.values():
        answer *= (value + 1)

    return answer - 1