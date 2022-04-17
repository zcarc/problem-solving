# 2022.02.09

# 내 풀이
def solution(x):
    answer = False
    p1 = -1
    n = 0
    tmp = x

    while p1 != 0:
        p1, p2 = divmod(tmp, 10)
        n += p2
        tmp = p1

    if x % n == 0:
        answer = True

    return answer


print(solution(13))


# 다른사람 풀이

# 풀이 1.
def s(x):
    return x % sum([int(char) for char in str(x)]) == 0