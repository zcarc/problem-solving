def solution():

    matrix = [list(map(int, input().split())) for _ in range(7)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]

    matrix[0][0] = 1

    cnt = 0

    def dfs(level):
        nonlocal cnt

        if matrix[6][6] == 1:
            cnt += 1
        else:
            for i in range(4):
                y = level[0] + dy[i]
                x = level[1] + dx[i]
                if 0 <= y <= 6 and 0 <= x <= 6:
                    if matrix[y][x] == 0:
                        matrix[y][x] = 1
                        dfs((y, x))
                        matrix[y][x] = 0

    dfs((0, 0))

    print(cnt)


solution()


# 정답