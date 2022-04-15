def solution():

    n = int(input())

    arr = [tuple(map(int, input().split())) for _ in range(n)]

    arr.sort(key=lambda x: x[1])

    end_time = arr[0][1]

    cnt = 1
    for i in range(1, n):
        if end_time <= arr[i][0]:
            end_time = arr[i][1]
            cnt += 1

    return cnt


print(solution())