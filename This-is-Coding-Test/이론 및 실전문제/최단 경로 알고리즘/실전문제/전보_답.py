import heapq

INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] * (n + 1) for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))


def dijkstra(start):
    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        base_weight, base_node = heapq.heappop(pq)

        if distance[base_node] < base_weight:
            continue

        for adjacency_node, adjacency_weight in graph[base_node]:
            sum_weight = base_weight + adjacency_weight

            if sum_weight < distance[adjacency_node]:
                distance[adjacency_node] = sum_weight
                heapq.heappush(pq, (sum_weight, adjacency_node))


dijkstra(c)

count_city = 0
max_time = 0

for d in distance:
    if d != INF:
        count_city += 1
        max_time = max(max_time, d)

# 시작 노드를 제외해야 하므로 -1
print(count_city - 1, max_time)