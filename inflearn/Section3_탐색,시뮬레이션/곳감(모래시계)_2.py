def solution():

    n = int(input())

    matrix = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        matrix.append(tmp)

    m = int(input())

    for _ in range(m):
        a, b, c = map(int, input().split())

        if b == 0:
            for i in range(c):
                popped = matrix[a - 1].pop(0)
                matrix[a - 1].append(popped)
        else:
            for i in range(c):
                popped = matrix[a - 1].pop()
                matrix[a - 1].insert(0, popped)

    mid = n // 2

    start = 0
    end = n

    # 모래시계 형태로 값 누적
    result = 0
    for i in range(n):
        for j in range(start, end):
            result += matrix[i][j]

        if i < mid:
            start += 1
            end -= 1
        elif i >= mid:
            start -= 1
            end += 1

    return result


print(solution())