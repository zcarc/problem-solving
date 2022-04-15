def solution():

    n = int(input())

    matrix = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        matrix.append(tmp)

    # 각 행과 열을 누적해서 가장 큰 값을 구함
    biggest = -2147000000
    for i in range(len(matrix)):
        tmp1 = 0
        tmp2 = 0
        for j in range(len(matrix[i])):
            tmp1 += matrix[i][j]
            tmp2 += matrix[j][i]

        if tmp1 > biggest:
            biggest = tmp1

        if tmp2 > biggest:
            biggest = tmp2

    # 대각선을 각각 누적하고 구했던 가장 큰 값과 비교해서 가장 큰 값을 구함
    tmp1 = 0
    tmp2 = 0
    for i in range(len(matrix[0])):
        tmp1 += matrix[i][i]
        tmp2 += matrix[len(matrix[0]) - 1 - i][i]

    if tmp1 > biggest:
        biggest = tmp1

    if tmp2 > biggest:
        biggest = tmp2

    # 가장 큰 값을 반환
    return biggest


print(solution())
