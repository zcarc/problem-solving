# 무한대 값
INF = int(1e9)

# 노드
n = int(input())

# 간선
m = int(input())

# 2차원 그래프
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선의 정보를 입력 받아서 초기화
for i in range(m):
    # a -> b 의 비용 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
# Dab = min(Dab, Dak + Dkb)
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('INFINITY')
        else:
            print(graph[a][b], end=' ')
    print()

# 플로이드 워셜 알고리즘
# N이 500 이하일 경우 사용하기 좋은 알고리즘이다.
# 시간 복잡도: O(N^3)