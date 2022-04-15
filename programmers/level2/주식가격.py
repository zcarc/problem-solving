def solution(prices):
    res = [0] * len(prices)

    stack = [(0, prices[0])]

    for i in range(1, len(prices)):
        while stack and stack[-1][1] > prices[i]:
            now = stack.pop()
            res[now[0]] = i - now[0]
        stack.append((i, prices[i]))

    while stack:
        now = stack.pop()
        res[now[0]] = (len(prices) - 1) - now[0]

    return res


print(solution([1, 2, 3, 4, 2, 2, 3]))