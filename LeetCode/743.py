import collections
import heapq


def s(times, n, k):

    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    priorityQueue = [(0, k)]

    dist = {}

    while priorityQueue:
        time, node = heapq.heappop(priorityQueue)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(priorityQueue, (alt, v))

    if len(dist) == n:
        return max(dist.values())
    else:
        return -1






