n = int(input())


def digit_sum(x):
    return sum(list(map(int, str(x))))


def solution(n):

    nums = list(map(int, input().split()))

    max_value = -2147000000
    answer = ''

    for e in nums:
        result = digit_sum(e)
        if result > max_value:
            max_value = result
            answer = e

    return answer


print(solution(n))