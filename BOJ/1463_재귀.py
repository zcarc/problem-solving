

# 백준에서 오답 (메모리 초과)
import sys
sys.setrecursionlimit(10 ** 6)

x = int(input())


def solution(x):

    dp = [0] * (x + 1)

    dp[2] = 1
    dp[3] = 1

    def dfs(x):

        if x % 2 == 0 and dp[x // 2] != 0:
            dp[x] = dp[x // 2] + 1
            return dp[x]
        elif x % 3 == 0 and dp[x // 3] != 0:
            dp[x] = dp[x // 3] + 1
            return dp[x]
        elif dp[x - 1] != 0:
            dp[x] = dp[x - 1] + 1
            return dp[x]

        dp[x] = dfs(x - 1) + 1
        if x % 2 == 0:
            dp[x] = min(dp[x], dfs(x // 2) + 1)
        elif x % 3 == 0:
            dp[x] = min(dp[x], dfs(x // 3) + 1)

        return dp[x]

    result = dfs(x)
    return result


print(solution(x))