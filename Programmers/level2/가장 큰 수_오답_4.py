def solution(numbers):

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    return ''.join(numbers)


print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0]))


# 테스트케이스 11 실패