from typing import List

n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))


def solution(n: int, array1: List[int], m: int, array2: List[int]):

    array1.sort()

    # 이진탐색 재귀
    def binary_search(array, target, start, end):
        if start > end:
            return None

        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            return binary_search(array, target, start, mid - 1)

        else:
            return binary_search(array, target, mid + 1, end)

    for e in array2:
        if binary_search(array1, e, 0, n - 1) is None:
            print('no', end=' ')
        else:
            print('yes', end=' ')


solution(n, array1, m, array2)
