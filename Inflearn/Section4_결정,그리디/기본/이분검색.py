def binary_search(arr, m):

    arr.sort()

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == m:
            return mid + 1
        elif arr[mid] > m:
            end = mid - 1
        else:
            start = mid + 1


def solution():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = binary_search(arr, m)

    return answer


print(solution())