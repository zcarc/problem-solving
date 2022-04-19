from collections import deque


def solution(priorities, location):

    dq = deque((i, v) for i, v in enumerate(priorities))

    cnt = 0

    while True:
        e = dq.popleft()

        if dq and e[1] < max(dq, key=lambda x: x[1])[1]:
            dq.append(e)
        else:
            cnt += 1
            if e[0] == location:
                return cnt


print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))
# print(solution([1,1,1,1], 2))
print(solution([1], 0))
print(solution([1, 1, 1], 2))
# print(solution([1,2], 1))
# print(solution([2, 1, 2, 1, 2, 1, 2, 1, 2], 1))
