def solution():

    matrix = [list(map(int, input().split())) for _ in range(10)]

    dy = [0, 0, -1]
    dx = [1, -1, 0]

    ch = [[0] * 10 for _ in range(10)]

    res = -1

    def dfs(level):
        nonlocal res

        if res != -1:
            return

        if level[0] == 0:
            res = level[1]
            return

        for k in range(3):
            y = level[0] + dy[k]
            x = level[1] + dx[k]
            if 0 <= y <= 9 and 0 <= x <= 9:
                if ch[y][x] == 0 and matrix[y][x] == 1:
                    ch[y][x] = 1
                    dfs((y, x))

    for i in range(9, 10):
        for j in range(10):
            if matrix[i][j] == 2:
                ch[i][j] = 1
                dfs((i, j))

    print(res)


solution()


# 정답
# 문제해설 참고


