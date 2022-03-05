def solution(s):
    arr = list(map(int, s.split(' ')))
    answer = ''
    answer += str(min(arr))
    answer += ' '
    answer += str(max(arr))

    return answer


def solution2(s):
    arr = list(map(int, s.split(' ')))
    return str(min(arr)) + ' ' + str(max(arr))