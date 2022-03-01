# def solution():
#
#     # n, m = map(int, input().split())
#     n, m = 4, 5
#
#     frame = [
#         [0, 0, 1, 1, 0],
#         [0, 0, 0, 1, 1],
#         [1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0],
#     ]
#
#     move_row = [-1, 1, 0, 0]
#     move_column = [0, 0, 1, -1]
#
#     visited = [[False] * m for _ in range(n)]
#
#     def dfs(row_index, column_index, column):
#         if column == 1:
#             return
#
#         visited[row_index][column_index] = True
#
#         for i in range(4):
#             next_move_row = row_index + move_row[i]
#             next_move_column = column_index + move_column[i]
#             if -1 < next_move_row < n and -1 < next_move_column < m:


    # for row_index, row in enumerate(frame):
    #     for column_index, column in enumerate(row):
