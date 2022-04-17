import itertools


def solution(numbers):

    permutations = []
    res = list(itertools.permutations(numbers, len(numbers)))
    for e in res:
        permutations.append(''.join(map(str, e)))

    permutations.sort(reverse=True)

    return permutations[0]


print(solution([3, 30, 34, 5, 9]))


# 테스트케이스 1 ~ 11 시간초과