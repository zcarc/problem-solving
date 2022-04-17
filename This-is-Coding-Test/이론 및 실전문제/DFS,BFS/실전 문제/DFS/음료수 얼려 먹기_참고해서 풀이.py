# n, m = 4, 5
# graph = [
#         [0, 0, 1, 1, 0],
#         [0, 0, 0, 1, 1],
#         [1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0],
#     ]


def solution():

    n, m = map(int, input().split())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    def dfs(row, col):
        if row <= -1 or n <= row or col <= -1 or m <= col:
            return False

        if graph[row][col] == 0:
            graph[row][col] = 1
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
            return True

        else:
            return False

    answer = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if dfs(i, j) == True:
                answer += 1

    return answer


print(solution())