from collections import deque


def solution(priorities, location):

    if len(priorities) == 1:
        return 1
    elif len(set(priorities)) == 1:
        return location + 1

    dq = deque((i, v) for i, v in enumerate(priorities))
    e = dq.popleft()

    if e[1] < max(dq, key=lambda x: x[1])[1]:
        print(True)

    while e[1] < max(dq, key=lambda x: x[1])[1]:
        dq.append(e)
        e = dq.popleft()

    dq.appendleft(e)

    for i, v in enumerate(dq):
        if v[0] == location:
            return i + 1


# print(solution([2,1,3,2], 2))
# print(solution([1,1,1,1], 2))
# print(solution([1], 1))
# print(solution([1,2], 1))
print(solution([2, 1, 2, 1, 2, 1, 2, 1, 2], 1))
