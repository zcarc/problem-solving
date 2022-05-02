def solution(s):
    # split() 함수는 괄호 안에 값을 넣지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나눈다.
    list_s = list(map(int, s.split()))
    return str(min(list_s)) + ' ' + str(max(list_s))


def solution2(s):
    arr = list(map(int, s.split(' ')))
    answer = ''
    answer += str(min(arr))
    answer += ' '
    answer += str(max(arr))

    return answer


def solution3(s):
    arr = list(map(int, s.split(' ')))
    return str(min(arr)) + ' ' + str(max(arr))