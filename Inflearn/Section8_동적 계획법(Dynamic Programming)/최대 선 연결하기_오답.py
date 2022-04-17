def solution():

    n = int(input())

    right = [0] + list(map(int, input().split()))
    left = sorted(right)

    dp = [0] * (n + 1)

    start_index = -1
    for i in range(1, n + 1):
        if right[i] == 1:
            start_index = i + 1
            dp[1] = 1
            break

    for i in range(2, n + 1):
        for j in range(start_index, n + 1):
            if left[i] == right[j]:
                dp[i] = dp[i - 1] + 1
                start_index = j + 1
                break

        if dp[i] == 0:
            dp[i] = dp[i - 1]

    return max(dp)


print(solution())



