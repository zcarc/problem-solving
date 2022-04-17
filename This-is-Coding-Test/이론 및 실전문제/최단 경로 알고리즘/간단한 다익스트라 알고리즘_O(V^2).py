import sys

input = sys.stdin.readline

# 무한대 값 설정 (1 * 10^9)
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())

# 시작 노드
start = int(input())

# 노드 정보 그래프
graph = [[] for i in range(n + 1)]

# 방문한 노드 확인 리스트
visited = [False] * (n + 1)

# 최단 거리 리스트 (테이블)
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a노드에서 b노드로 가는 비용이 c
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서 해당 노드에 도달하는 거리가 가장 최단거리인 노드의 인덱스를 반환
def get_smallest_node_index():
    # 각 노드들의 도달하는 최단거리를 비교하기 위한 변수
    min_value = INF

    # 반복이 끝나면 가장 최단거리 인덱스가 저장될 변수
    index = 0

    # 모든 노드를 순회하면서 방문하지 않은 노드 중에서 거리를 기록하며 비교하면서 최단거리 인덱스를 찾기 위한 반복문
    for i in range(1, n + 1):
        if distance[i] < min_value and visited[i] is not True:
            min_value = distance[i]
            index = i

    return index


# 엔트리 포인트
def dijkstra(start):
    # 시작 값을 0으로 설정하고 방문처리
    distance[start] = 0
    visited[start] = True

    # start에 인접한 노드들의 최단 거리 연산 (distance)
    for node, weight in graph[start]:
        distance[node] = weight

    # 현재 노드와 연결된 다른 노드들의 최소비용을 갱신하기 위해서
    # 시작 노드를 제외한 전체 노드에 대한 반복
    for _ in range(n - 1):
        # 방문하지 않은 노드 중에 가장 최단 거리 노드를 가져온 뒤에 방문 처리한다.
        smallest_index = get_smallest_node_index()
        visited[smallest_index] = True

        # 현재 노드와 연결된 다른 노드를 확인해서 최소비용을 갱신
        for node, weight in graph[smallest_index]:
            cost = distance[smallest_index] + weight
            if cost < distance[node]:
                distance[node] = cost


# 다익스트라 알고리즘 실행
dijkstra(start)

# 모든 노드의 최단거리를 출력하기 위한 반복문
for d in distance[1:]:
    # 도달할 수 없는 노드라면 무한을 출력
    if d == INF:
        print('INFINITY')
    # 도달할 수 있는 노드라면 노드의 거리를 출력
    else:
        print(d)


# 시간복잡도: O(V^2)
# 총 O(V)번에 걸쳐서 최단거리가 가장 짧은 노드를 매번 선형 탐색해야하고,
# 현재 노드와 연결된 노드를 매번 일일이 확인하기 때문이다.
# 전체 노드 개수가 5,000개 이하하면 이 코드로 풀 수 있다.
# 하지만 10,000개를 넘어간다면 이 코드로 해결하기 어렵다.