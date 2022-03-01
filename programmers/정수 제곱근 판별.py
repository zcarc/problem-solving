# 2022.02.11

# 내 풀이
def solution(n):

    sqrt = n ** (1 / 2)
    if int(sqrt) == sqrt:
        answer = (int(sqrt) + 1) ** 2
    else:
        answer = -1

    return answer


# 다른사람 풀이

# 풀이 1
def s(n):

    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        answer = (int(sqrt) + 1) ** 2
    else:
        answer = -1

    return answer
