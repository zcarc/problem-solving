from collections import deque


def solution():

    n, m = map(int, input().split())

    graph = [[0] * (n + 1) for _ in range(n + 1)]

    degree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1

        degree[b] += 1

    dq = deque()
    for i in range(1, n + 1):
        if degree[i] == 0:
            dq.append(i)

    while dq:
        now = dq.popleft()
        print(now, end=' ')
        for i in range(1, n + 1):
            if graph[now][i] == 1:
                degree[i] -= 1
                if degree[i] == 0:
                    dq.append(i)


solution()