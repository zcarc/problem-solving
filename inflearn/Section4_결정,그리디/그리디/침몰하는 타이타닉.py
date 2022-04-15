from collections import deque


def solution():

    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    arr.sort()

    dq = deque(arr)

    cnt = 0
    while dq:
        if len(dq) > 1 and dq[0] + dq[-1] <= m:
            dq.popleft()
            dq.pop()
        else:
            dq.pop()

        cnt += 1

    return cnt


print(solution())