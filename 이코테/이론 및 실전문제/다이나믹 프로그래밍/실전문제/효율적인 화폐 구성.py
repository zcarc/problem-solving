n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))


def solution(n, m, arr):

    dp = [10001] * (m + 1)
    dp[0] = 0
    
    for i in range(len(arr)):
        for j in range(arr[i], m + 1):
            if dp[j - arr[i]] != 10001:
                dp[j] = min(dp[j], dp[j - arr[i]] + 1)

    if dp[m] == 10001:
        return -1
    else:
        return dp[m]


print(solution(n, m, arr))

