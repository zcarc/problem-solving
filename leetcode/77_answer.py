import itertools
from typing import List


# 풀이 1. DFS로 풀이
def combine(n: int, k: int) -> List[List[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])
            return

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)

    return results


# 풀이 2. itertools 모듈로 풀이
def combine2(n: int, k: int) -> List[List[int]]:
    return list(map(list, itertools.combinations(range(1, n + 1), k)))


print(combine2(4, 2))