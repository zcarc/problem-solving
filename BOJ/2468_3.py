import sys

sys.setrecursionlimit(10 ** 6)


def solution():

    n = int(input())

    matrix = [[0] * n for _ in range(n)]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    ch = [[0] * n for _ in range(n)]

    biggest = -2147000000

    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] > biggest:
                biggest = tmp[j]

            matrix[i][j] = tmp[j]

    cnt = 0

    res = -2147000000

    def dfs(level):
        nonlocal cnt

        for k in range(4):
            y = level[0] + dy[k]
            x = level[1] + dx[k]
            if 0 <= y <= n - 1 and 0 <= x <= n - 1:
                if ch[y][x] == 0:
                    ch[y][x] = -1
                    dfs((y, x))

    for h in range(biggest):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == h:
                    ch[i][j] = h

        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0:
                    ch[i][j] = -1
                    dfs((i, j))

                    cnt += 1

        if cnt > res:
            res = cnt

        cnt = 0

        for i in range(n):
            for j in range(n):
                if ch[i][j] == -1:
                    ch[i][j] = 0

    return res


print(solution())


