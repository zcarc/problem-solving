import sys


def solution(board):
    biggest = -sys.maxsize

    dy = [-1, 0, -1]
    dx = [0, -1, -1]

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            smallest = sys.maxsize
            for k in range(3):
                y = i + dy[k]
                x = j + dx[k]
                print((i, j), (y, x))
                smallest = min(smallest, board[y][x])
            board[i][j] = smallest + 1
            biggest = max(biggest, board[i][j])

    return biggest ** 2


board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
print(solution(board))
