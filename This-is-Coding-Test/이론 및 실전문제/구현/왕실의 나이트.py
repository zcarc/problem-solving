
def solution():

    # ex) c2
    input_data = input()

    column = int(ord(input_data[0]) - ord('a') + 1)
    row = int(input_data[1])

    # 상하좌우
    steps = [
        [-1, -2], [1, -2],
        [-1, 2], [1, 2],
        [-2, -1], [-2, 1],
        [2, -1], [2, 1]
    ]

    answer = 0

    for step in steps:
        next_column = column + step[0]
        next_row = row + step[1]
        if 1 <= next_column <= 8 and 1 <= next_row <= 8:
            answer += 1

    return answer


print(solution())

