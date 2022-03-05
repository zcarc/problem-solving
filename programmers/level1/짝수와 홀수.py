# 2022.02.10

# 내 풀이
def solution(num):
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'

    return answer


print(solution(4))


# 다른사람 풀이
def s(num):
    if num % 2:
        answer = 'Odd'
    else:
        answer = 'Even'

    return answer


print(s(4))