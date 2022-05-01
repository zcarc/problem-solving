import itertools


def solution(nums):
    nums = set(itertools.combinations(nums, len(nums) // 2))

    tmp = []
    for e in map(set, nums):
        tmp.append(len(e))

    return max(tmp)


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))

