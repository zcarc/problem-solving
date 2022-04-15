def solution():

    n, m = map(int, input().split())

    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1

    ch = [0] * (n + 1)
    cnt = 0

    def dfs(vertex):
        nonlocal cnt

        if vertex == n:
            cnt += 1
        else:
            for i in range(1, n + 1):
                if ch[i] == 1:
                    continue

                if graph[vertex][i] == 0:
                    continue

                ch[i] = 1
                dfs(i)
                ch[i] = 0

    ch[1] = 1
    dfs(1)

    print(cnt)


solution()