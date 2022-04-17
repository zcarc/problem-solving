def solution():

    n = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    dp = [[0] * n for _ in range(n)]

    def dfs(level):
        y, x = level

        if dp[y][x] > 0:
            return dp[y][x]

        if y == 0 and x == 0:
            dp[y][x] = matrix[y][x]
        elif y == 0:
            dp[y][x] = dfs((y, x - 1)) + matrix[y][x]
        elif x == 0:
            dp[y][x] = dfs((y - 1, x)) + matrix[y][x]
        else:
            dp[y][x] = min(dfs((y - 1, x)), dfs((y, x - 1))) + matrix[y][x]

        return dp[y][x]

    return dfs((n - 1, n - 1))


print(solution())


# 답안참고 풀이
