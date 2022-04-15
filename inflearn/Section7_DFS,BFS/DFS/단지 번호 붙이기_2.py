def solution():

    n = int(input())

    matrix = [list(map(int, input())) for _ in range(n)]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    res = []

    cnt = 0

    def dfs(level):
        nonlocal cnt

        matrix[level[0]][level[1]] = 0
        cnt += 1

        for k in range(4):
            y = level[0] + dy[k]
            x = level[1] + dx[k]
            if 0 <= y <= n - 1 and 0 <= x <= n - 1:
                if matrix[y][x] == 1:
                    dfs((y, x))

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                cnt = 0
                dfs((i, j))
                res.append(cnt)


    print(len(res))

    for e in sorted(res):
        print(e)


solution()


# 답안 참고 풀이
# 답안에서는 직접 푼 방법과 다르게 이미 방문한 노드를
# 0 으로 할당하는 부분과 cnt 를 1 증가 시키는 부분의 중복이 없다.