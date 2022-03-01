import collections
from typing import List


# 풀이 1. DFS 그래프로 풀이
def s(tickets: List[List[str]]):

    graph = collections.defaultdict(list)
    for from_, to_ in sorted(tickets):
        graph[from_].append(to_)

    print(f'graph: {graph}')
    answer = []

    def dfs(airline):
        while graph[airline]:
            dfs(graph[airline].pop(0))
        answer.append(airline)

    dfs('JFK')

    return answer[::-1]


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets2 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets3 = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]

print(s(tickets))
# print(s(tickets2))
# print(s(tickets3))


# 풀이 2. 스택 연산으로(pop()) 큐 연산(pop(0)) 최적화
def s2(tickets):

    graph = collections.defaultdict(list)
    for from_, to_ in sorted(tickets, reverse=True):
        graph[from_].append(to_)

    answer = []

    def dfs(airline):
        while graph[airline]:
            dfs(graph[airline].pop())
        answer.append(airline)

    dfs('JFK')

    return answer[::-1]


print(s2(tickets))


# 풀이 3. 스택으로 반복 풀이
def s3(tickets):

    graph = collections.defaultdict(list)
    for from_, to_ in sorted(tickets):
        graph[from_].append(to_)

    answer = []
    stack = ['JFK']

    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        answer.append(stack.pop())

    return answer[::-1]