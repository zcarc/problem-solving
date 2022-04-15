def solution():

    n = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    dp = [[0] * n for _ in range(n)]

    dp[0][0] = matrix[0][0]

    def dfs(level):
        y, x = level

        if (0 > y or y > n - 1) or (0 > x or x > n - 1):
            return 2147000000

        if dp[y][x] > 0:
            return dp[y][x]

        dp[y][x] = min(dfs((y - 1, x)), dfs((y, x - 1))) + matrix[y][x]
        return dp[y][x]

    return dfs((n - 1, n - 1))


print(solution())


# 정답
