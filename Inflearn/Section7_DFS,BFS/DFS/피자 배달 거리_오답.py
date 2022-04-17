def solution():

    n, m = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(4)]

    house = []
    pizza = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                house.append((i, j))
            elif matrix[i][j] == 2:
                pizza.append((i, j))

    arrival = [0] * m

    comb = []

    smallest = 2147000000

    def dfs(level, start):
        nonlocal smallest

        if level == m:
            comb.append(arrival.copy())
        else:
            for i in range(start, len(pizza)):
                arrival[level] = pizza[i]
                dfs(level + 1, i + 1)

    dfs(0, 0)

    sum_dis = []

    for pizza_row in comb:
        tmp1 = []
        for h in house:
            tmp2 = []
            for p in pizza_row:
                dis = abs(h[0] - h[1]) + abs(p[0] - p[1])
                tmp2.append(dis)
            tmp1.append(sum(tmp2))
        sum_dis.append(tmp1)

    print(f'len(sum_dis): {len(sum_dis)}')


solution()


