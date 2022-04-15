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
            # n까지 이어지는 경로 출력
            for x in path:
                print(x, end=' ')
            print()
        else:
            for i in range(1, n + 1):
                if ch[i] == 1:
                    continue

                if graph[vertex][i] == 0:
                    continue

                ch[i] = 1
                path.append(i)

                dfs(i)

                ch[i] = 0
                path.pop()

    # vertex 1부터 시작하므로 1을 할당(이미 방문한 노드로 식별)
    ch[1] = 1

    # n까지 이어지는 경로를 담는 리스트
    path = [1]

    dfs(1)

    print(cnt)


solution()