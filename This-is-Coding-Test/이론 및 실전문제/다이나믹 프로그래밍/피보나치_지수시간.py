
def fibo(n):
    global cnt
    cnt += 1
    if n == 1 or n == 2:
        return 1

    return fibo(n - 1) + fibo(n - 2)


print(fibo(30))

# 시간복잡도가 O(N^2) 이라서 개선해 줄 필요가 있는 코드이다.
# f(30)이라면 이 코드의 연산은 약 10억번을 해야한다.
