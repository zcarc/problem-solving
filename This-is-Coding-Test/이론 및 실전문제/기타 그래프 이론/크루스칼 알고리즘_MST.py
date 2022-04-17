def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution():
    v, e = map(int, input().split())

    parent = [0] * (v + 1)
    for i in range(1, v + 1):
        parent[i] = i

    edges = []
    result = 0

    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(result)


solution()


# 신장 트리
# - 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않은 부분 그래프를 말한다.

# 최소 신장 트리
# - 신장 트리 중에서 최소 비용으로 만들어진 트리

# 크루스칼 알고리즘
# - 최소 신장 트리를 구하는 알고리즘
# A부터 특정 지점까지 한 번씩 연결해서 이동하는 최소 비용을 구할 때 사용된다.
# 여기서 MST의 초기 그래프는 무방향이어야한다.
# 크루스킬 알고리즘은 그리디 알고리즘으로 분류된다.

# 최종 신장 트리의 간선의 개수는 "노드의 개수 -1개" 이다.
# 트리 자료구조도 간선의 개수가 "노드의 개수 -1개" 이다.


# 시간복잡도: O(ElogE)
# E: Edge