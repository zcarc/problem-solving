def solution():

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # 전체 행렬 검사
    for i in range(9):
        row_check = [0] * 10
        col_check = [0] * 10
        for j in range(9):
            row_check[sudoku[i][j]] = 1
            col_check[sudoku[j][i]] = 1

        # 각 행, 열에 1 ~ 9가 모두 하나씩 있다면 그 합은 9가 된다.
        if sum(row_check) != 9 or sum(col_check) != 9:
            return 'NO'

    # 전체 그룹단위 검사
    for i in range(3):
        for j in range(3):
            group_check = [0] * 10
            for k in range(3):
                for s in range(3):
                    group_check[sudoku[i * 3 + k][j * 3 + s]] = 1

            if sum(group_check) != 9:
                return 'NO'

    return 'YES'


print(solution())





