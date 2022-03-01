# 2022.02.12

# 내 풀이
def solution(n):
    answer = ''
    arr = ['수', '박']

    for i in range(n):
        answer += arr[i % 2]

    return answer


# print(solution(3))


# 다른사람 풀이

# 풀이 1.
def solution2(n):

    s = '수박' * n
    return s[:n]


# 풀이 2.
def solution3(n):

    return '수박' * (n // 2) + '수' * (n % 2)


print(solution3(9))