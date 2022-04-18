from collections import deque


def solution(progresses, speeds):
    length = len(progresses)
    dq = deque()
    res = []

    for i in range(length):

        cnt = 1
        while progresses[i] + (speeds[i] * cnt) < 100:
            cnt += 1

        if not dq:
            dq.append(cnt)
        else:
            if dq[0] >= cnt:
                dq.append(cnt)
            else:
                res.append(len(dq))
                dq.clear()
                dq.append(cnt)

    if dq:
        res.append(len(dq))

    return res


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
