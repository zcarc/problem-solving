def solution():

    n = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    dp = [[0] * n for _ in range(n)]

    dp[0][0] = matrix[0][0]

    for i in range(1):
        for j in range(1, n):
            dp[i][j] = dp[i][j - 1] + matrix[i][j]
            dp[j][i] = dp[j - 1][i] + matrix[j][i]

    def dfs(level):
        y, x = level

        if dp[y][x] > 0:
            return dp[y][x]

        dp[y][x] = min(dfs((y - 1, x)), dfs((y, x - 1))) + matrix[y][x]
        return dp[y][x]

    return dfs((n - 1, n - 1))


print(solution())


# 정답
