from collections import deque

# n, m = 3, 3
# graph = [
#     [1, 1, 0],
#     [0, 1, 0],
#     [0, 1, 1]
# ]


def solution():

    n, m = map(int, input().split())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    # 상하좌우
    move_row = [-1, 1, 0, 0]
    move_col = [0, 0, -1, 1]

    def bfs(row, col):
        queue = deque([(row, col)])
        while queue:
            row, col = queue.popleft()
            for i in range(4):
                next_move_row = row + move_row[i]
                next_move_col = col + move_col[i]
                if -1 < next_move_row < n and -1 < next_move_col < m:
                    if graph[next_move_row][next_move_col] == 1:
                        graph[next_move_row][next_move_col] = graph[row][col] + 1
                        queue.append((next_move_row, next_move_col))

    bfs(0, 0)

    return graph[n - 1][m - 1]


print(solution())

