def solution():

    n = int(input())

    arr = [0] + list(map(int, input().split()))

    dp = [0] * (n + 1)
    dp[1] = 1

    res = -2147000000

    for i in range(2, n + 1):
        biggest = 0

        for j in range(i - 1, 0, -1):
            if arr[i] > arr[j] and biggest < dp[j]:
                biggest = dp[j]

        dp[i] = biggest + 1

        if dp[i] > res:
            res = dp[i]

    return res


print(solution())


# 답안참고 풀이