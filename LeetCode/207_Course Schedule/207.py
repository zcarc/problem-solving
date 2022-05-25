# def s(numCourses, prerequisites):
#
#     def dfs(n):
#         if len(prerequisites) == 0 and n == 0:
#             return True
#         elif n < 0:
#             return False
#
#         for _ in prerequisites:
#             return dfs(n - len(prerequisites.pop()))
#
#     return dfs(numCourses)
#
#
# print(s(2, [[1, 0]]))
import collections


# 풀이 1. DFS
def s(numCourses, prerequisites):

    graph = collections.defaultdict(list)
    for x, y in prerequisites:
        graph[x].append(y)

    visited = set()

    def dfs(key):
        if key in visited:
            return False

        visited.add(key)

        for x in graph[key]:
            if not dfs(x):
                return False

        visited.remove(key)
        graph[key] = []

        return True

    for key in list(graph):
        if not dfs(key):
            return False

    return True


# 풀이 2. DFS로 가지치기
def s2(numCourses, prerequisites):

    graph = collections.defaultdict(list)
    for x, y in prerequisites:
        graph[x].append(y)

    visited = set()
    pruning = set()

    def dfs(key):
        if key in visited:
            return False
        if key in pruning:
            return True

        visited.add(key)

        for x in graph[key]:
            if not dfs(x):
                return False

        visited.remove(key)
        pruning.add(key)

        return True

    for key in list(graph):
        if not dfs(key):
            return False

    return True



