def solution():

    n, m = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(n)]

    house = []
    pizza = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                house.append((i, j))
            elif matrix[i][j] == 2:
                pizza.append((i, j))

    combi = [0] * m

    min_dis = 2147000000

    def dfs(level, start):

        if level == m:
            nonlocal min_dis
            total = 0

            for i in range(len(house)):
                x1 = house[i][0]
                y1 = house[i][1]
                smallest = 2147000000

                for j in combi:
                    x2 = pizza[j][0]
                    y2 = pizza[j][1]
                    dis = abs(x1 - x2) + abs(y1 - y2)
                    smallest = min(smallest, dis)

                total += smallest

            if total < min_dis:
                min_dis = total

        else:
            for i in range(start, len(pizza)):
                combi[level] = i
                dfs(level + 1, i + 1)

    dfs(0, 0)

    print(min_dis)


solution()


# 이 문제는 다수의 피자집에서 특정 피자집들을 선택해야하므로 조합을 사용해야한다.
# 답안 참고 풀이