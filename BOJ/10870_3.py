n = int(input())


def solution(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n]


print(solution(n))