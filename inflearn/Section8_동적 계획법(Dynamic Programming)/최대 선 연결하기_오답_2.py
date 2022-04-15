def solution():

    n = int(input())

    right = [0] + list(map(int, input().split()))
    left = sorted(right)

    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        cnt = 0
        start_index = 1
        for j in range(i, n + 1):
            for k in range(start_index, n + 1):
                if left[j] == right[k]:
                    cnt += 1
                    start_index = k + 1
                    break

        dp[i] = cnt

    print(dp)

    return max(dp)


print(solution())



