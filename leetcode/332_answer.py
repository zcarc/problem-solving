import collections
from typing import List


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    print(f'tickets: {tickets}')
    print(f'sorted(tickets): {sorted(tickets)}')
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    print(f'graph: {graph}')
    route = []

    def dfs(a):
        # 첫 번째 값을 읽어 어휘순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('JFK')
    # 다시 뒤집어 어휘순 결과로
    return route[::-1]


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets2 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets3 = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "ATL"]]
print(findItinerary(tickets))
print(findItinerary(tickets3))


# 풀이 3
def findItinerary3(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    print(f'graph: {graph}')
    route, stack = [], ['JFK']
    while stack:
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    # 다시 뒤집어 어휘순 결과로
    return route[::-1]


print(findItinerary3(tickets3))