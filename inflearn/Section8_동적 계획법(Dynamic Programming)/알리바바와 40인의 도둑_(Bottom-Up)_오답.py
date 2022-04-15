import sys


def solution():

    n = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    dy = [0, 1]
    dx = [1, 0]

    cnt = matrix[0][0]

    for i in range(n):
        for j in range(n):
            min_height = 2147000000
            min_y = -1
            min_x = -1
            for k in range(2):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y <= n - 1 and 0 <= x <= n - 1:
                    if matrix[y][x] < min_height:
                        min_height = matrix[y][x]
                        min_y = y
                        min_x = x

            cnt += min_height

            if min_y == n - 1 and min_x == n - 1:
                print(cnt)
                sys.exit(0)

            if min_y != i:
                break


solution()