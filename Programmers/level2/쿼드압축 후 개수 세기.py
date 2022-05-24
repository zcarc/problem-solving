def solution(arr):

    res = [0, 0]

    def dfs(y, x, len_arr):
        first_value = arr[y][x]
        for i in range(y, y + len_arr):
            for j in range(x, x + len_arr):
                if arr[i][j] != first_value:
                    half_len_arr = len_arr // 2
                    dfs(y, x, half_len_arr)
                    dfs(y, x + half_len_arr, half_len_arr)
                    dfs(y + half_len_arr, x, half_len_arr)
                    dfs(y + half_len_arr, x + half_len_arr, half_len_arr)
                    return

        res[first_value] += 1

    dfs(0, 0, len(arr))

    return res


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))
