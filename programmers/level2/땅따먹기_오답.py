def solution(land):
    max_value = -2147000000
    answer = 0
    max_index = -1
    prev_index = -1

    for row in land:
        max_value = -2147000000
        for i, e in enumerate(row):
            if e > max_value and i != prev_index:
                max_value = e
                max_index = i
        answer += max_value
        prev_index = max_index

    return answer


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))