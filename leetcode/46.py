import itertools
from typing import List


# 풀이 1. DFS로 풀이
def permute(nums: List[int]) -> List[List[int]]:
    answer = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            answer.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)

    return answer


nums = [1, 2, 3]
# print(permute(nums))


# 풀이 2. itertools 모듈로 순열 생성
def permute2(nums):
    print(type(itertools.permutations(nums)))
    return list(map(list, itertools.permutations(nums)))


print(permute2(nums))


# itertools.permutations 는 구현의 효율성 성능을 위해 사용했다.
# 이 모듈은 반복자 생성에 최적화된 효율적인 기능들을 제공한다.

# 이미 잘 구현된 라이브러리라서 직접 구현함에 따른 버그 발생 가능성이 낮고,
# 효율적으로 설계된 C 라이브러리라서 속도에도 이점이 있다.