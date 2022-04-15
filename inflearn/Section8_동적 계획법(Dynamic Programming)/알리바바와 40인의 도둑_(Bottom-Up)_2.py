def solution():

    n = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    dp = [[0] * n for _ in range(n)]

    dp[0][0] = matrix[0][0]

    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]
        dp[j][0] = dp[j - 1][0] + matrix[j][0]

    for i in range(1, n):
        for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    return dp[n - 1][n - 1]


print(solution())


# 답안 참고