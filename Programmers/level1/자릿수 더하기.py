# 2022.02.11

# 내 풀이
def solution(n):
    return sum([int(x) for x in str(n)])


# print(solution(123))
# print(solution(987))


# 다른사랆 풀이

# 풀이 1. 재귀
def s(n):
    if n < 10:
        return n
    return n % 10 + s(n // 10)


print(s(123))


# 풀이 2. 반복문
def s2(n):
    answer = 0

    while n != 0:
        answer = answer + n % 10
        n = n // 10

    return answer


print(s2(123))