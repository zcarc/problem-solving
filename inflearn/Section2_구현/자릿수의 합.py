n = int(input())


def digit_sum(x):
    return sum(list(map(int, str(x))))


def solution(n):

    nums = list(map(int, input().split()))

    arr = []
    for x in nums:
        arr.append(digit_sum(x))

    max_value = -2147000000
    answer = -1
    for i, e in enumerate(arr):
        if e > max_value:
            max_value = e
            answer = i

    return nums[answer]


print(solution(n))