def solution():

    n, m = map(int, input().split())

    arr = [tuple(map(int, input().split())) for _ in range(n)]

    dp = [0] * (m + 1)

    for i in range(n):
        weight, value = arr[i]
        for j in range(weight, m + 1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[m]


print(solution())


# 정답
# 문제해설 참고풀이 (답 확인 X)