import itertools


def solution():

    n, f = map(int, input().split())

    b = [1] * n

    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i

    arr = list(range(1, n + 1))
    for p in itertools.permutations(arr):
        acc = 0

        for level, x in enumerate(p):
            acc += (x * b[level])

        if acc == f:
            for x in p:
                print(x, end=' ')
            break


solution()