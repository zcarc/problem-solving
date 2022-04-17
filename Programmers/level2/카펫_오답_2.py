def solution(brown, yellow):

    for i in range((brown // 2) - 1, 0, -1):
        for j in range(1, brown // 2):
            if i * j == brown + yellow:
                return [i, j]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
print(solution(10, 4))


