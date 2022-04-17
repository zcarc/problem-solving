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

    cnt = 0
    while True:
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for k in range(4):
                        y = i + dy[k]
                        x = j + dx[k]
                        if 0 <= y <= n - 1 and 0 <= x <= m - 1:
                            if ch[y][x] == 0 and matrix[y][x] == 1:
                                dq.append((y, x))
                                ch[y][x] = 1

        if not dq:
            break

        while dq:
            now = dq.popleft()
            for k in range(4):
                y = now[0] + dy[k]
                x = now[1] + dx[k]
                if 0 <= y <= n - 1 and 0 <= x <= m - 1:
                    if matrix[y][x] == 0:
                        matrix[y][x] = 1

        cnt += 1

        ch = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                return -1

    return cnt


print(solution())


