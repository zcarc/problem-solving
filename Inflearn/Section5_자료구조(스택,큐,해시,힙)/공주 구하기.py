from collections import deque


def solution():

    n, k = map(int, input().split())

    dq = deque(list(range(1, n + 1)))

    cnt = k
    while len(dq) > 1:
        if cnt == 1:
            dq.popleft()
            cnt = k

        else:
            dq.append(dq.popleft())
            cnt -= 1

    return dq.pop()


print(solution())
