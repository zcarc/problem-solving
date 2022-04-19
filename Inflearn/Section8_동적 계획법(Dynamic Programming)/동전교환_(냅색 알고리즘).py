def solution():

    n = int(input())

    coins = list(map(int, input().split()))

    m = int(input())

    dp = [0] + [1000] * m

    for i in range(n):
        coin = coins[i]
        for j in range(coin, m + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[m]


print(solution())


# 정답
# 문제해설 참고풀이 (답 확인 X)