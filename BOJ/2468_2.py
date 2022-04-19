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

    def dfs(level, h):
        ch[level[0]][level[1]] = 1

        for k in range(4):
            y = level[0] + dy[k]
            x = level[1] + dx[k]
            if 0 <= y <= n - 1 and 0 <= x <= n - 1:
                if ch[y][x] == 0 and matrix[y][x] > h:
                    dfs((y, x), h)

    for h in range(biggest):
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and matrix[i][j] > h:
                    dfs((i, j), h)
                    cnt += 1

        res = max(res, cnt)
        cnt = 0

        ch = [[0] * n for _ in range(n)]

    return res


print(solution())