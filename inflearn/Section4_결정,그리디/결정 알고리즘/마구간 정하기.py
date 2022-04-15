def get_count(arr, mid):

    left = arr[0]

    cnt = 1
    for i in range(1, len(arr)):
        right = arr[i]

        if right - left >= mid:
            left = arr[i]
            cnt += 1

    return cnt


def solution():

    n, c = map(int, input().split())

    arr = []
    for _ in range(n):
        x = int(input())
        arr.append(x)

    arr.sort()

    start = 1
    end = max(arr)

    answer = 0
    while start <= end:
        mid = (start + end) // 2

        cnt = get_count(arr, mid)

        if cnt >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer


print(solution())