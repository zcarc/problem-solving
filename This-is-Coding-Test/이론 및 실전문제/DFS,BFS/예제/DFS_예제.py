# DFS 메서드 정의
def dfs(graph, node, visited):
    # 현재 노드를 방문 처리
    visited[node] = True
    print(node, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for vertex in graph[node]:
        if not visited[vertex]:
            dfs(graph, vertex, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
# graph에서 0번째 배열은 비어두어서 하나 더 필요하므로 길이를 9로 생성
visited = [False] * 9

# DFS 호출
dfs(graph, 1, visited)