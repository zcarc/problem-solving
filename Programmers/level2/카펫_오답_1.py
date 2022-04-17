def solution(brown, yellow):

    total = brown + yellow
    root = int(total ** (1 / 2))

    res = []
    if root ** 2 == total:
        res.append(root)
    else:
        res.append(root + 1)

    for i in range(max(brown, yellow), 0, -1):
        if res[0] * i == total:
            print(res[0], i, total)
            res.append(i)

    return res


print(solution(24, 24))