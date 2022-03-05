# 2022.02.09

# 내 풀이
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x * (i + 1))

    return answer


# print(solution(2, 5))
# print(solution(4, 3))
# print(solution(-4, 2))


# 다른사람 풀이
# 풀이 1.
def s(x, n):
    return [(i * x) + x for i in range(n)]


print(s(-4, 5))

