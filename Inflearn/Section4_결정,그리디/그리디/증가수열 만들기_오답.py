from collections import deque


def solution():

    n = int(input())

    arr = list(map(int, input().split()))

    dq = deque(arr)

    p = dq.popleft()

    result = 'L'
    cnt = 1
    convention = 0
    position = 'left'

    if p < dq[-1]:
        convention = dq[-1] - p
        result += 'R'
        cnt += 1
        p = dq.pop()
        position = 'right'

    elif p < dq[0]:
        convention = dq[0] - p
        result += 'L'
        cnt += 1
        p = dq.popleft()
        position = 'left'

    while dq:
        if position == 'right':
            if dq[0] - p == convention:
                result += 'L'
                cnt += 1
                p = dq.popleft()
            else:
                dq.popleft()
            position = 'left'

        elif position == 'left':
            if dq[-1] - p == convention:
                result += 'R'
                cnt += 1
                p = dq.pop()
            else:
                dq.pop()
            position = 'right'

    return str(cnt) + '\n' + result


print(solution())



