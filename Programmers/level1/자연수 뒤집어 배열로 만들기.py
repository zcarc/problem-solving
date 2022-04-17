# 2022.02.11

# 내 풀이
def solution(n):
    n = list(str(n))
    return list(map(int, n[::-1]))


# 내 풀이 2
def s(n):
    return list(map(int, str(n)[::-1]))


# 다른 사람 풀이
def s2(n):
    return list(map(int, reversed(str(n))))