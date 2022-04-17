def solution():

    n, m = map(int, input().split())

    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        dp[a][b] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j] == float('inf'):
                print('M', end=' ')
            else:
                print(dp[i][j], end=' ')
        print()


solution()


# 정답해설 참고