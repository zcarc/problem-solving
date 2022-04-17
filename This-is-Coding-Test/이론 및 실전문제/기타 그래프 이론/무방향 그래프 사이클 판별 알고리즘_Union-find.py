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

    cycle = False

    for _ in range(e):
        a, b = map(int, input().split())

        if find_parent(parent, a) == find_parent(parent, b):
            cycle = True
            break
        else:
            union_parent(parent, a, b)

    if cycle:
        print('사이클이 있습니다.')
    else:
        print('사이클이 없습니다.')


solution()


# 서로소 집합(Disjoint Sets) 자료구조를 이용한 무방향 그래프 사이클 판별
# Union-find 자료구조 라고도 불린다.