def solution():

    n = int(input())

    arr = [tuple(map(int, input().split())) for _ in range(n)]

    arr.sort(reverse=True)

    largest = arr[0][1]

    cnt = 1
    for i in range(1, n):
        if arr[i][1] > largest:
            largest = arr[i][1]
            cnt += 1

    return cnt


print(solution())
