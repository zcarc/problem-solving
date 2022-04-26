def solution(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]

    return total


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
