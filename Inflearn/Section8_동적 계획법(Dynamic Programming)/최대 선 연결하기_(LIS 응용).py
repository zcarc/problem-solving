def solution():

    n = int(input())

    arr = [0] + list(map(int, input().split()))

    dp = [0] * (n + 1)

    dp[1] = 1

    res = -2147000000

    for i in range(2, n + 1):
        biggest = 0
        for j in range(i - 1, 0, - 1):
            if arr[i] > arr[j]:
                if dp[j] > biggest:
                    biggest = dp[j]

        dp[i] = biggest + 1

        if dp[i] > res:
            res = dp[i]

    return max(dp)


print(solution())


# 정답
# 문제해설 참고