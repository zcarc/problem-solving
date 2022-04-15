def solution():

    n = int(input())

    arr = [0] + list(map(int, input().split()))

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        biggest = -2147000000

        for j in range(1, i):
            if arr[i] > arr[j]:
                biggest = max(biggest, dp[j])

        if biggest > -2147000000:
            dp[i] = biggest + 1
        else:
            dp[i] = 1

    longest = -2147000000
    for e in dp:
        if e > longest:
            longest = e

    return longest


print(solution())


# 정답
# 문제해설 풀이