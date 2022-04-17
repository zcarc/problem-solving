def solution():

    n, m = map(int, input().split())

    arr = [tuple(map(int, input().split())) for _ in range(n)]

    arr.sort(key=lambda x: x[1])

    dp = [0] * (m + 1)
    for i in range(n):
        dp[arr[i][1]] = arr[i][0]

    for index_i, value_i in enumerate(arr):
        for _, value_j in enumerate(arr[index_i + 1:]):
            dp[value_i[1] + value_j[1]] = max(dp[value_i[1] + value_j[1]], dp[value_i[1]] + dp[value_j[1]])

    return dp[m]


print(solution())


