def solution():

    n = int(input())

    dp = [0] * (n + 1)

    def dfs(level):

        if dp[level] != 0:
            return dp[level]

        if level == 2:
            dp[level] = 2
            return 2
        elif level == 1:
            dp[level] = 1
            return 1

        res = dfs(level - 1) + dfs(level - 2)
        dp[level] = res

        return res

    return dfs(n)


print(solution())


# 정답
# 9번 라인에서 메모이제이션한 값을 가지치기 해야한다.
# 하지 않으면 시간초과가 된다.