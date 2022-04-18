def solution(progresses, speeds):

    if len(progresses) == 0 and progresses[0] == 0:
        return [0]

    length = len(progresses)
    stack = []
    res = []

    for i in range(length):

        cnt = 1
        while progresses[i] + (speeds[i] * cnt) < 100:
            cnt += 1

        if not stack:
            stack.append(cnt)
        else:
            if stack[-1] >= cnt:
                stack.append(cnt)
            else:
                res.append(len(stack))
                stack.clear()
                stack.append(cnt)

    if stack:
        res.append(len(stack))

    return res


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
