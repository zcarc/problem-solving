def solution():

    n = int(input())

    matrix = [list(map(int, input())) for _ in range(n)]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    res = []

    cnt = 0

    def dfs(level):
        nonlocal cnt

        for k in range(4):
            y = level[0] + dy[k]
            x = level[1] + dx[k]
            if 0 <= y <= n - 1 and 0 <= x <= n - 1:
                if matrix[y][x] == 1:
                    matrix[y][x] = 0
                    cnt += 1
                    dfs((y, x))

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                cnt += 1
                dfs((i, j))
                res.append(cnt)
                cnt = 0

    print(len(res))

    for e in sorted(res):
        print(e)


solution()


# 정답
# 답안을 참고한 풀이에서는 코드에서 몇가지 중복을 제거한 풀이이다.