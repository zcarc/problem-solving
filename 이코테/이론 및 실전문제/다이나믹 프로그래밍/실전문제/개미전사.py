from typing import List

x = int(input())
arr = list(map(int, input().split()))


def solution(x: int, arr: List[int]):

    dp = [0] * x

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, x):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

    return dp[x - 1]


print(solution(x, arr))


