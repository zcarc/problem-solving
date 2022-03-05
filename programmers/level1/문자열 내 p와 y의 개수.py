# 2022.02.13

# 내 풀이.
def solution(s):

    answer = False

    p = 0
    y = 0
    for x in s:
        if x.upper() == 'P':
            p += 1
        elif x.upper() == 'Y':
            y += 1

    if p == y:
        answer = True

    return answer


# 다른사람 풀이

# 풀이 1.
def solution2(s):
    return s.upper().count('P') == s.upper().count('Y')


print(solution2('pPyY'))