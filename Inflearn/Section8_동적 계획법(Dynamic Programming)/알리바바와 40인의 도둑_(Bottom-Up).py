def solution():

    n = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    dy = [-1, 0]
    dx = [0, -1]

    dp = [[0] * n for _ in range(n)]

    dp[0][0] = matrix[0][0]

    for i in range(1):
        for j in range(1, n):
            dp[i][j] = dp[i][j - 1] + matrix[i][j]
            dp[j][i] = dp[j - 1][i] + matrix[j][i]

    for i in range(1, n):
        for j in range(1, n):
            min_energy = 2147000000
            for k in range(2):
                y = i + dy[k]
                x = j + dx[k]
                if dp[y][x] < min_energy:
                    min_energy = dp[y][x]

            dp[i][j] = min_energy + matrix[i][j]

    return dp[n - 1][n - 1]


print(solution())


# 정답
# 문제해설 참고