from collections import deque


def solution():
    v, e = map(int, input().split())

    # 진입차수 리스트
    indegree = [0] * (v + 1)

    # 인접리스트 (2차원 리스트)
    graph = [[] for _ in range(v + 1)]

    # 방향 그래프 모든 간선 정보 입력받기
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    def topological_sort():
        q = deque()
        for i in range(1, v + 1):
            if indegree[i] == 0:
                q.append(i)

        result = []
        while q:
            current = q.popleft()
            result.append(current)

            for target in graph[current]:
                indegree[target] -= 1
                if indegree[target] == 0:
                    q.append(target)

        for x in result:
            print(x, end=' ')

    topological_sort()


solution()

# 위상정렬은 인접리스트 그래프와 진입차수(indegree)리스트가 필요하고
# 진입차수가 0인 노드를 큐에 넣는다.
# 큐에서 노드를 꺼내고 result에 추가한다음
# 꺼낸 노드가 가리키고 있는 노드를 그래프에서 찾고
# 해당 노드의 indegree를 -1 해주고 결과가 0과 같다면 큐에 해당 노드를 삽입한다.
# 이것을 큐가 빌 때까지 반복한다.

# 위상정렬은 "선수과목을 고려한 학습 순서 설정"과 같은 정렬을 수행할 때 사용된다.


# 방향성 비순환 그래프: DAG(Directed Acyclic Graph) 일 때만 사용가능하다.

# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 볼 수 있다.
# 사이클에 포함된 원소 중에서 어떠한 워노도 큐에 들어가지 못하기 때문이다.

# 위상 정렬은 여러가지 답이 존재할 수 있다.
# 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우가 있다면 여러 가지 답이 존재한다.

# 큐로 구현하는 방법과 스택을 활용해서 DFS로 구현하는 방법이 있다.

# 시간복잡도: O(V+E)