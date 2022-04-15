from collections import deque


def solution():

    n, k = map(int, input().split())

    dq = deque(list(range(1, n + 1)))

    while dq:
        for _ in range(k - 1):
            dq.append(dq.popleft())
        dq.popleft()

        if len(dq) == 1:
            return dq.pop()


print(solution())
