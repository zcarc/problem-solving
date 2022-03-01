import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    base, target, weight = map(int, input().split())
    graph[base].append((target, weight))


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


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])

# 최악의 경우: O(ElogV)
# E: Edge, V: Vertex

# 삽입, 삭제: O(logN)