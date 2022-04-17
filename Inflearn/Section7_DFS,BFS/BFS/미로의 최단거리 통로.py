import collections


def solution():

    matrix = [list(map(int, input().split())) for _ in range(7)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]

    dq = collections.deque()
    dq.append((0, 0))

    distance = [[0] * 7 for _ in range(7)]
    distance[0][0] = 0

    matrix[0][0] = 1

    while dq:
        now = dq.popleft()
        for i in range(4):
            y = now[0] + dy[i]
            x = now[1] + dx[i]
            if 0 <= y <= 6 and 0 <= x <= 6:
                if matrix[y][x] == 0:
                    dq.append((y, x))
                    distance[y][x] = distance[now[0]][now[1]] + 1
                    matrix[y][x] = 1

    if distance[6][6] > 0:
        print(distance[6][6])
    else:
        print(-1)


solution()


