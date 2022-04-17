def solution():

    n, m = map(int, input().split())

    dp = [0] * (m + 1)

    for i in range(n):
        weight, value = map(int, input().split())
        for j in range(weight, m + 1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[m]


print(solution())


# 정답
# 답안해설 참고