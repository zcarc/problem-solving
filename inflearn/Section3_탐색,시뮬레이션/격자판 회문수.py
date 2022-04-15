def solution():

    grid = [list(map(int, input().split())) for _ in range(7)]

    cnt = 0
    for i in range(7):
        for j in range(3):
            row_is_palindrome = True
            col_is_palindrome = True
            for k in range(5 // 2):
                if grid[i][j + k] != grid[i][j + (4 - k)]:
                    row_is_palindrome = False

                if grid[j + k][i] != grid[j + (4 - k)][i]:
                    col_is_palindrome = False

            if row_is_palindrome:
                cnt += 1

            if col_is_palindrome:
                cnt += 1

    return cnt


print(solution())