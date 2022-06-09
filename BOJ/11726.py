n = int(input())


def solution(n):

    if n == 1:
        return 1

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n] % 10007


print(solution(n))


# 참고:
# https://yabmoons.tistory.com/506