a = int(input())
b = list(map(int, input().split()))

cnt = 0


def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True

    for j in range(2, n):
        if n % j == 0:
            return False
    return True


for i in b:
    if isPrime(i):
        cnt += 1

print(cnt)
