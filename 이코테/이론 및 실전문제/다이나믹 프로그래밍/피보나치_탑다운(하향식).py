# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
dp = [0] * 100

# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1

    # 이미 계산된 적 있는 문제라면 그대로 반환
    if dp[x] != 0:
        return dp[x]

    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    dp[x] = fibo(x - 1) + fibo(x - 2)

    return dp[x]


print(fibo(99))


# 다이나믹 프로그래밍에서 메모이제이션은 탑다운 방식에 국한된 표현이다.
# 메모이제이션으로 배열이나 리스트말고 딕셔너리를 활용할 수도 있다.
# 모두가 아닌 일부의 작은 문제에 대해 해답만 필요한 경우 사전 자료형이 효과적일 수 있다.

# 가능하다면 탑다운보다는 바텀업 방식을 사용하는것을 권장한다.
# 시스템상 재귀 함수의 스택 크기가 한정되어 있을 수 있기 때문이다.