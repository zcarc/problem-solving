def solution():

    n = int(input())

    arr = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        arr.append(tmp)

    result = []
    mid = n // 2
    for i in range(mid):
        for j in range(mid - i, mid + i + 1):
            result.append(arr[i][j])
            result.append(arr[n - 1 - i][j])

    for i in range(mid, mid + 1):
        for j in range(n):
            result.append(arr[i][j])

    return sum(result)


print(solution())
