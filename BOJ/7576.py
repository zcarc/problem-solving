import collections


def solution():

    m, n = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(n)]

    tmp = True
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                tmp = False
                break

    if tmp:
        return 0

    dq = collections.deque()

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    ch = [[0] * m for _ in range(n)]

    res = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                dq.append((i, j))

    while True:
        for _ in range(len(dq)):
            now = dq.popleft()
            for k in range(4):
                y = now[0] + dy[k]
                x = now[1] + dx[k]
                if 0 <= y <= n - 1 and 0 <= x <= m - 1:
                    if matrix[y][x] == 0:
                        matrix[y][x] = 1
                        dq.append((y, x))
                        ch[y][x] = ch[now[0]][now[1]] + 1
                        res = ch[y][x]

        if not dq:
            break

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                return -1

    return res


print(solution())


