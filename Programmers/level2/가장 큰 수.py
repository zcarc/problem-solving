def solution(numbers):

    numbers = list(map(str, numbers))
    # 0 이상 1000 이하이므로 * 3을 해준다.
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # 0이 연속적으로 나올 수 있으니 (ex: '000')
    # 정수형으로 바뀐 뒤 문자열로 바꾼다.
    return str(int(''.join(numbers)))


print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0]))

