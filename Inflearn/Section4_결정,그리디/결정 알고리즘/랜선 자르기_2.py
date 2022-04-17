def quotient_count(arr, mid):

    cnt = 0
    for e in arr:
        cnt += e // mid

    return cnt


def binary_search_custom(arr, n):

    big_line = max(arr)

    start = 1
    end = big_line

    answer = 0
    while start <= end:
        mid = (start + end) // 2

        cnt = quotient_count(arr, mid)

        if cnt >= n:
            start = mid + 1
            answer = mid
        elif cnt < n:
            end = mid - 1

    return answer


def solution():

    k, n = map(int, input().split())

    arr = []
    for _ in range(k):
        length = int(input())
        arr.append(length)

    answer = binary_search_custom(arr, n)

    return answer


print(solution())