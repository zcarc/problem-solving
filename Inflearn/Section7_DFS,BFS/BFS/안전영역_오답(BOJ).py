import collections


def solution():

    n = int(input())

    matrix = [[0] * n for _ in range(n)]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    dq = collections.deque()

    ch = [[0] * n for _ in range(n)]

    smallest = 2147000000
    biggest = -2147000000

    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] < smallest:
                smallest = tmp[j]

            if tmp[j] > biggest:
                biggest = tmp[j]

            matrix[i][j] = tmp[j]

    height = smallest

    cnt = 0

    res = -2147000000

    while height <= biggest:
        for i in range(n):
            for j in range(n):
                if height == matrix[i][j]:
                    ch[i][j] = height

        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0:
                    dq.append((i, j))
                    ch[i][j] = -1

                    while dq:
                        now = dq.popleft()
                        for k in range(4):
                            y = now[0] + dy[k]
                            x = now[1] + dx[k]
                            if 0 <= y <= n - 1 and 0 <= x <= n - 1:
                                if ch[y][x] == 0:
                                    dq.append((y, x))
                                    ch[y][x] = -1

                    cnt += 1

        if cnt > res:
            res = cnt

        cnt = 0

        for i in range(n):
            for j in range(n):
                if ch[i][j] == -1:
                    ch[i][j] = 0

        height += 1

    return res


print(solution())


# 인프런 채점에서는 정답이나 백준에서는 오답

# 모든 높이가 2라면 0이 아니라 1이 나와야한다.
# 아무 곳도 잠기지 않으면 인접한 영역의 높이는 0이 아니라 1이기 때문이다.
