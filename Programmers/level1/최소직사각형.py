def solution(sizes):

    max_width = -2147000000
    max_height = -2147000000

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

        max_width = max(max_width, sizes[i][0])
        max_height = max(max_height, sizes[i][1])

    return max_width * max_height


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
