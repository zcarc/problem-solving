import collections


def solution():
    n = int(input())

    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    dq = collections.deque()
    dq.append((n // 2, n // 2))

    ch = [[0] * n for _ in range(n)]
    ch[n // 2][n // 2] = 1

    total = matrix[n // 2][n // 2]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    level = 0

    while True:
        if level == n // 2:
            break

        size = len(dq)
        for i in range(size):
            now = dq.popleft()
            for j in range(4):
                y = now[0] + dy[j]
                x = now[1] + dx[j]
                if ch[y][x] == 0:
                    total += matrix[y][x]
                    dq.append((y, x))
                    ch[y][x] = 1

        level += 1

    print(total)


solution()


# 답안 참고 풀이