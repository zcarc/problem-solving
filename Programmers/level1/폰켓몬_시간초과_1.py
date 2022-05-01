import itertools
from collections import defaultdict


def solution(nums):

    nums = list(itertools.combinations(nums, len(nums) // 2))

    tmp = []
    for e in nums:
        dic = defaultdict(int)
        for x in e:
            dic[x] = 1
        tmp.append(len(dic.keys()))

    return max(tmp)


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))

