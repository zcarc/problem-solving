def solution():

    n, m = map(int, input().split())

    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(graph[i][j], end=' ')
        print()


solution()


# input
# 5 5
# 1 2
# 1 3
# 2 4
# 3 4
# 4 5
