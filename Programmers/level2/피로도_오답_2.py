from collections import deque


def solution(k, dungeons):

    dungeons.sort(reverse=True)

    dq = deque(dungeons)

    prev = []

    cnt = 0
    while dq:
        if k >= dq[0][0]:
            cnt += 1
            k -= dq[0][1]
            prev = dq.popleft()
            print(f'if dq[0]: {prev}, k: {k}, prev: {prev}')
        else:
            cnt -= 1
            k += prev[1]
            dq.append(prev)
            print(f'else dq[0]: {dq[0]}, k: {k}, prev: {prev}')

    print(k)

    return cnt


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
