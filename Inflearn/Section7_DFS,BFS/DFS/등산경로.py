def solution():

    n = int(input())

    matrix = [list(map(int, input().split())) for _ in range(n)]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    smallest = 2147000000
    biggest = -2147000000

    smallest_index = (-1, -1)
    biggest_index = (-1, -1)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] < smallest:
                smallest = matrix[i][j]
                smallest_index = (i, j)

            if matrix[i][j] > biggest:
                biggest = matrix[i][j]
                biggest_index = (i, j)

    ch = [[0] * n for _ in range(n)]
    ch[smallest_index[0]][smallest_index[1]] = 1

    cnt = 0

    def dfs(level):
        nonlocal cnt

        if level[0] == biggest_index[0] and level[1] == biggest_index[1]:
            cnt += 1
        else:
            for i in range(4):
                y = level[0] + dy[i]
                x = level[1] + dx[i]
                if 0 <= y <= n - 1 and 0 <= x <= n - 1:
                    if ch[y][x] == 0 and matrix[level[0]][level[1]] < matrix[y][x]:
                        ch[y][x] = 1
                        dfs((y, x))
                        ch[y][x] = 0

    dfs((smallest_index[0], smallest_index[1]))

    print(cnt)


solution()


# 정답
# 이 풀이는 모든 입력을 받고 나서 또 다른 반복문에서 가장 작은, 큰 값의 위치를 찾아내고,
# 답안을 참고한 풀이는 입력을 받음과 동시에 가장 작은, 큰 값의 위치를 찾아낸다.