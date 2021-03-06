dp = [0] * 100

dp[1] = 1
dp[2] = 1
n = 99

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])


# 다이나믹 프로그래밍의 전형적인 형태는 바텀업 방식이다.
# 가능하다면 탑다운보다는 바텀업 방식을 사용하는것을 권장한다.
# 시스템상 재귀 함수의 스택 크기가 한정되어 있을 수 있기 때문이다.