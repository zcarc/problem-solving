# 2022.02.13

# 내 풀이.
def solution(s):
    answer = False

    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            answer = True

    return answer


# 다른사람 풀이

# 풀이 1.
def solution2(s):
    return s.isdigit() and len(s) in (4, 6)

