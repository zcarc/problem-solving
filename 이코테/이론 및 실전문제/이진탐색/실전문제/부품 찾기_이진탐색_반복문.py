from typing import List

n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))


def solution(n: int, array1: List[int], m: int, array2: List[int]):

    array1.sort()

    # 이진탐색 반복문
    def binary_search(array, target, start, end):

        while start <= end:
            mid = (start + end) // 2

            if array[mid] == target:
                return mid

            elif array[mid] > target:
                end = mid - 1

            else:
                start = mid + 1

        return None

    for e in array2:
        if binary_search(array1, e, 0, n - 1) is None:
            print('no', end=' ')
        else:
            print('yes', end=' ')


solution(n, array1, m, array2)
