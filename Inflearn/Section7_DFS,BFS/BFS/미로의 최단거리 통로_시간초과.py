import collections


def solution():

    matrix = [list(map(int, input().split())) for _ in range(7)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]

    dq = collections.deque()
    dq.append((0, 0))

    ch = [[0] * 7 for _ in range(7)]
    ch[0][0] = 1

    while True:
        if matrix[6][6] > 0:
            print(matrix[6][6])
            break

        size = len(dq)
        for _ in range(size):
            now = dq.popleft()
            for j in range(4):
                y = now[0] + dy[j]
                x = now[1] + dx[j]
                if 0 <= y <= 6 and 0 <= x <= 6:
                    if ch[y][x] == 0 and matrix[y][x] != 1:
                        dq.append((y, x))
                        matrix[y][x] = matrix[now[0]][now[1]] + 1
                        ch[y][x] = 1


solution()


# 도착하지 못했을 경우 -1를 출력하지 못해서 무한루프에 걸린다.