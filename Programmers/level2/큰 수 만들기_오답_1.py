def solution(number, k):

    if k == 1:
        return sorted(number, reverse=True)[0]

    _number = number[:-(k - 1)]
    _number = sorted(list(_number), reverse=True)
    _number = ''.join(_number[: - k])
    number = number[-(k - 1):]

    return _number + number


