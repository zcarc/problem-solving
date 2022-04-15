def solution():

    n = int(input())

    coins = list(map(int, input().split()))

    m = int(input())

    dp = [1000] * (m + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(coins[i], m + 1):
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

    return dp[m]


print(solution())


# 정답
# 답안해설 참고