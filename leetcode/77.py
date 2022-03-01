from typing import List


def s(n: int, k: int) -> List[List[int]]:
    answer = []

    def dfs(elements: List[int], start: int, k: int):
        if k == 0:
            answer.append(elements[:])
            return

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)

    return answer


# print(s(4, 2))
# print(s(5, 3))