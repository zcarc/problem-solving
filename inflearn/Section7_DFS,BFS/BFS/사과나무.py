import collections


def solution():
    n = int(input())

    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    dq = collections.deque()
    dq.append((n // 2, n // 2))

    ch = collections.defaultdict(int)
    ch[(n // 2, n // 2)] = 1

    total = 0

    y = [-1, 0, 1, 0]
    x = [0, 1, 0, -1]

    flag = True
    while dq and flag:
        now = dq.popleft()
        total += matrix[now[0]][now[1]]
        for i in range(4):
            if now[0] + y[i] < 0 or now[1] + x[i] < 0:
                flag = False
                break

            if ch[(now[0] + y[i], now[1] + x[i])] == 0:
                dq.append((now[0] + y[i], now[1] + x[i]))
                ch[(now[0] + y[i], now[1] + x[i])] = 1

    while dq:
        now = dq.popleft()
        total += matrix[now[0]][now[1]]

    print(total)


solution()


# 정답
# 정답이지만 답안의 풀이가 더 괜찮아보인다.