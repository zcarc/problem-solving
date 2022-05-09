import itertools


def solution(d, budget):

    for i in range(len(d), 0, -1):
        tmp = itertools.combinations(d, i)
        for e in tmp:
            if sum(e) == budget:
                return i


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
