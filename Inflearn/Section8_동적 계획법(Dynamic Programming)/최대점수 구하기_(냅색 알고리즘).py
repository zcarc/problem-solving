def solution():

    n, m = map(int, input().split())

    dp = [0] * (m + 1)

    for i in range(n):
        value, time = map(int, input().split())
        for j in range(m, time - 1, -1):
            dp[j] = max(dp[j], dp[j - time] + value)

    return dp[m]


print(solution())


# 정답
# 문제해설 참고