def solution():

    n = int(input())

    matrix = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        matrix.append(tmp)

    # 각 행과 열을 삽입
    sum_arr = []
    for i in range(len(matrix)):
        tmp1 = []
        tmp2 = []
        for j in range(len(matrix[i])):
            tmp1.append(matrix[i][j])
            tmp2.append(matrix[j][i])

        sum_arr.append(tmp1)
        sum_arr.append(tmp2)

    # 대각선 삽입
    tmp1 = []
    tmp2 = []
    for i in range(len(matrix[0])):
        tmp1.append(matrix[i][i])
        tmp2.append(matrix[len(matrix[0]) - 1 - i][i])

    sum_arr.append(tmp1)
    sum_arr.append(tmp2)

    # 삽입된 2차원 배열들의 합을 구하고 1차원 배열에 추가
    result = list(map(sum, sum_arr))

    # 1차원 배열에서 가장 큰 값 반환
    return max(result)


print(solution())