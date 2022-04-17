def solution(numbers):

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 2, reverse=True)

    return ''.join(numbers)


print(solution([3, 30, 34, 5, 9]))


# 테스트케이스 1 ~ 6, 11 실패