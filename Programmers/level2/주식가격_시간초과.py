from collections import deque


def solution(prices):
    dq = deque(prices)

    res = []
    while dq:
        now = dq.popleft()
        for i in range(len(dq)):
            if now > dq[i]:
                res.append(i + 1)
                break
        else:
            res.append(len(dq))

    return res


print(solution([1, 2, 3, 2, 3]))