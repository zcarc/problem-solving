from typing import List


def s(candidates: List[int], target: int) -> List[List[int]]:
    answer: List[List[int]] = []

    def dfs(target_d: int, index: int, path: List[int]):
        if target_d < 0:
            return
        if target_d == 0:
            answer.append(path)
            return

        for i in range(index, len(candidates)):
            dfs(target_d - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])

    return answer


candidates = [2, 3, 6, 7]
target = 7
# print(s(candidates, target))
print(s([2], 1))