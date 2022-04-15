import sys


def solution():

    n = int(input())

    arr = list(map(int, input().split()))

    total = sum(arr)

    def dfs(level, acc):
        if level == n:
            if acc == (total - acc):
                print('YES')
                sys.exit(0)
        else:
            dfs(level + 1, acc + arr[level])
            dfs(level + 1, acc)

    dfs(0, 0)

    print('NO')


solution()