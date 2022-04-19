n = int(input())


def fibo(n):
    if n == 1 or n == 2:
        return 1

    return fibo(n - 1) + fibo(n - 2)


if n == 0:
    print(n)
else:
    print(fibo(n))
