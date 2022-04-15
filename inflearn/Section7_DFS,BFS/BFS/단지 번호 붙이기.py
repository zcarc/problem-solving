import collections


def solution():

    n = int(input())

    matrix = [list(map(int, input())) for _ in range(n)]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    res = []

    cnt = 0

    dq = collections.deque()

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                dq.append((i, j))
                cnt += 1
                matrix[i][j] = 0

                while dq:
                    now = dq.popleft()
                    for k in range(4):
                        y = now[0] + dy[k]
                        x = now[1] + dx[k]
                        if 0 <= y <= n - 1 and 0 <= x <= n - 1:
                            if matrix[y][x] == 1:
                                dq.append((y, x))
                                cnt += 1
                                matrix[y][x] = 0

                res.append(cnt)
                cnt = 0

    print(len(res))
    for e in sorted(res):
        print(e)


solution()


# 정답