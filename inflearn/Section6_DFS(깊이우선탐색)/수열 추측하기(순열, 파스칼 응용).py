import sys


def solution():

    n, f = map(int, input().split())

    p = [0] * n
    b = [1] * n
    ch = [0] * (n + 1)

    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i

    def dfs(level, acc):
        if level == n and acc == f:
            for x in p:
                print(x, end=' ')
            sys.exit(0)
        else:
            for i in range(1, n + 1):
                if ch[i] == 0:
                    ch[i] = 1
                    p[level] = i
                    dfs(level + 1, acc + (p[level] * b[level]))
                    ch[i] = 0
            return

    dfs(0, 0)


solution()