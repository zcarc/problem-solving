def solution():

    n = int(input())

    matrix = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        matrix.append(tmp)

    m = int(input())

    commands = []
    for _ in range(m):
        tmp = list(map(int, input().split()))
        commands.append(tmp)

    for a, b, c in commands:
        if b == 0:
            for i in range(c):
                popped = matrix[a - 1].pop(0)
                matrix[a - 1].append(popped)
        else:
            for i in range(c):
                popped = matrix[a - 1].pop()
                matrix[a - 1].insert(0, popped)

    mid = n // 2

    # 모래시계 형태로 값 누적 (정중앙 제외)
    result = 0
    for i in range(mid):
        for j in range(i, n - i):
            result += matrix[i][j]
            result += matrix[n - 1 - i][j]

    # 정중앙 값 누적
    result += matrix[mid][mid]

    return result


print(solution())