from collections import deque


def solution():

    n, m = map(int, input().split())

    patients = [(i, v) for i, v in enumerate(map(int, input().split()))]

    dq = deque(patients)

    cnt = 0
    while True:
        popped = dq.popleft()

        if any(popped[1] < patient[1] for patient in dq):
            dq.append(popped)

        else:
            cnt += 1
            if popped[0] == m:
                return cnt


print(solution())

