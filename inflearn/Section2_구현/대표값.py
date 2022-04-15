n = int(input())
arr = list(map(int, input().split()))


def solution(n, arr):

    avg = int((sum(arr) / n) + 0.5)

    min_value = 2147000000
    answer_index = -1
    answer_value = -1

    for index, value in enumerate(arr):
        tmp = abs(value - avg)

        if tmp < min_value:
            min_value = tmp
            answer_value = value
            answer_index = index

        elif tmp == min_value:
            if value > answer_value:
                answer_value = value
                answer_index = index

    return avg, answer_index + 1


print(*solution(n, arr))