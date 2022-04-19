a = int(input())
b = int(input())

l = []


def isPrime(n):
    if n == 1:
        return False

    for j in range(2, int(n ** (1 / 2)) + 1):
        if n % j == 0:
            return False
    else:
        return True


def findMinArray(arr):
    m = arr[0]
    for i in arr:
        if m > i:
            m = i
    return m


def sumArray(arr):
    cnt = 0
    for i in arr:
        cnt += i
    return cnt


for i in range(a, b + 1):
    if isPrime(i):
        l.append(i)


if len(l) != 0:
    print(sumArray(l))
    print(findMinArray(l))
else:
    print(-1)

