import sys


def solution(board):
    biggest = -sys.maxsize

    dy = [-1, 0, -1]
    dx = [0, -1, -1]

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] > 0:
                smallest = sys.maxsize
                for k in range(3):
                    y = i + dy[k]
                    x = j + dx[k]
                    smallest = min(smallest, board[y][x])
                board[i][j] = smallest + 1
                biggest = max(biggest, board[i][j])

    if biggest == -sys.maxsize:
        m = -1
        for row in board:
            m = max(row)
            if m == 0:
                return 0
            else:
                return 1

    return biggest * biggest


# board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
# board = [[0, 0], [1, 0]]
board = [[0, 0], [0, 1]]
print(solution(board))


# 참고
# https://onlydev.tistory.com/65
# https://minnnne.tistory.com/16
# https://soobarkbar.tistory.com/164
# https://j-sik.tistory.com/129