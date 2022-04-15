def solution():

    n = int(input())

    matrix = [[0] * n for _ in range(n)]

    smallest = 2147000000
    biggest = -2147000000

    smallest_index = (-1, -1)
    biggest_index = (-1, -1)

    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(n):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = (i, j)

            if arr[j] > biggest:
                biggest = arr[j]
                biggest_index = (i, j)

            matrix[i][j] = arr[j]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

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


# 답안 참고 풀이
# 이 방법은 입력을 받음과 동시에 가장 작은, 큰 값의 위치를 찾아낸다.