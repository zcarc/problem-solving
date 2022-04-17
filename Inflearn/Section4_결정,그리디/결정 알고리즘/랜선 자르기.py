
def solution():

    k, n = map(int, input().split())

    arr = []
    for _ in range(k):
        length = int(input())
        arr.append(length)

    big_line = max(arr)

    start = 1
    end = big_line

    answer = 0
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for e in arr:
            cnt += e // mid

        if cnt >= n:
            start = mid + 1
            answer = mid
        elif cnt < n:
            end = mid - 1

    return answer


print(solution())