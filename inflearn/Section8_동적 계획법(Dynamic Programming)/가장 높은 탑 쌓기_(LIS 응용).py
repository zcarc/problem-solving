def solution():

    n = int(input())

    bricks = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        bricks.append((a, b, c))

    bricks.sort(reverse=True)

    dp = [0] * n

    dp[0] = bricks[0][1]

    res = -2147000000

    for i in range(1, n):
        max_height = 0
        for j in range(i - 1, -1, -1):
            if bricks[i][2] < bricks[j][2] and dp[j] > max_height:
                max_height = dp[j]

        dp[i] = max_height + bricks[i][1]

        res = max(res, dp[i])

    return res


print(solution())


# 답안참고 풀이