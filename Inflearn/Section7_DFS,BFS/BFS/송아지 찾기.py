from collections import deque


def solution():
    maximum = 10000

    s, e = map(int, input().split())

    dq = deque()
    dq.append(s)

    distance = [0] * (maximum + 1)
    distance[s] = 0

    check = [0] * (maximum + 1)
    check[s] = 1

    while dq:
        now = dq.popleft()
        if now == e:
            break
        for next in (now - 1, now + 1, now + 5):
            if 1 <= next <= maximum:
                if check[next] == 0:
                    dq.append(next)
                    distance[next] = distance[now] + 1
                    check[next] = 1

    print(distance[e])


solution()


