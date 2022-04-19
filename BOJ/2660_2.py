import sys


def solution():

    n = int(input())

    dp = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = 0

    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        dp[a][b] = 1
        dp[b][a] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    arr_biggest = []
    for i in range(1, n + 1):
        arr_biggest.append(max(dp[i][1:]))

    smallest = min(arr_biggest)
    arr_smallest = []
    for i, v in enumerate(arr_biggest):
        if v == smallest:
            arr_smallest.append(i + 1)

    print(smallest, len(arr_smallest))
    print(' '.join(map(str, arr_smallest)))


solution()