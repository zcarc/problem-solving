def solution(n):
    a = 1
    d = 1
    sum_arithmetic_sequence = n * ((2 * a) + ((n - 1) * d)) // 2

    matrix = [[0] * (n + 1) for _ in range(n + 1)]

    top = 1
    left = 1
    bottom = n
    right = 0

    def dfs(level, direction):
        if level > sum_arithmetic_sequence:
            return
        else:
            nonlocal top, left, bottom, right
            if direction == 1:
                for i in range(top, bottom + 1):
                    level += 1
                    matrix[i][left] = level
                top += 1
                left += 1
                dfs(level, 2)
            elif direction == 2:
                for i in range(left, bottom - right + 1):
                    level += 1
                    matrix[bottom][i] = level
                bottom -= 1
                dfs(level, 3)
            elif direction == 3:
                for i in range(bottom, top - 1, -1):
                    level += 1
                    matrix[i][i - right] = level
                right += 1
                top += 1
                dfs(level, 1)

    dfs(0, 1)

    return matrix


print(solution(5))
