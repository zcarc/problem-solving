def solution():

    n = int(input())

    dp = [0] * (n + 1)

    def dfs(level):

        if dp[level] > 0:
            return dp[level]

        if level == 2 or level == 1:
            dp[level] = level
            return level

        dp[level] = dfs(level - 1) + dfs(level - 2)
        return dp[level]

    return dfs(n)


print(solution())


# 답안 참고 풀이