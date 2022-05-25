from typing import List


def s(nums: List[int]) -> List[List[int]]:
    answer: List[List[int]] = []

    def dfs(index, path):
        answer.append(path)

        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])

    return answer


print(s([1, 2, 3]))