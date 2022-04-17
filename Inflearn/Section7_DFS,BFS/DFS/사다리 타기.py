def solution():

    matrix = [list(map(int, input().split())) for _ in range(10)]

    dy = [0, 0, 1]
    dx = [1, -1, 0]

    ch = [[0] * 10 for _ in range(10)]

    col_arrival = [0] * 10

    start_col = -1
    res = -1

    def dfs(level):
        nonlocal res

        if res != -1:
            return

        if matrix[level[0]][level[1]] == 2:
            res = start_col
            return

        if level[0] == 9:
            col_arrival[start_col] = 1
            return

        for k in range(3):
            y = level[0] + dy[k]
            x = level[1] + dx[k]
            if 0 <= y <= 9 and 0 <= x <= 9:
                if col_arrival[start_col] == 0 and ch[y][x] == 0 and 1 <= matrix[y][x] <= 2:
                    ch[y][x] = 1
                    dfs((y, x))

    for i in range(1):
        for j in range(10):
            if matrix[i][j] == 1:
                start_col = j
                ch[i][j] = 1
                dfs((i, j))

                ch = [[0] * 10 for _ in range(10)]

    print(res)


solution()


# 정답
# 정답이지만 이 방법은 0행에서 1인 값인 모든 열을 밑으로 탐색한다.
# 문제해설에서는 이것보다 더 좋은 방법을 알려준다.
# 마지막 도착지점이 2인 지점에서 출발해서 역으로 올라가서 도착한 지점이 시작지점이 된다.
# 사다리 타기의 도착지점의 값이 2인 경우는 1개이므로 이 지점부터 출발하면 바로 해결이 가능하다.