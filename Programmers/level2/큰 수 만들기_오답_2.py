from itertools import combinations


def solution(number, k):

    res = list(combinations(number, len(number) - k))
    return ''.join(sorted(res, reverse=True)[0])


