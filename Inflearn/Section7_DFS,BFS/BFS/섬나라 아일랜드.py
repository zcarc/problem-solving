import collections


def solution():

    n = int(input())

    matrix = [list(map(int, input().split())) for _ in range(n)]

    # 시계방향, 대각선
    dy = [-1, 0, 1, 0, -1, 1, 1, -1]
    dx = [0, 1, 0, -1, 1, 1, -1, -1]

    dq = collections.deque()

    cnt = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                dq.append((i, j))
                matrix[i][j] = 0

                while dq:
                    now = dq.popleft()
                    for k in range(8):
                        y = now[0] + dy[k]
                        x = now[1] + dx[k]
                        if 0 <= y <= n - 1 and 0 <= x <= n - 1:
                            if matrix[y][x] == 1:
                                dq.append((y, x))
                                matrix[y][x] = 0
                cnt += 1

    print(cnt)


solution()


# 정답