import collections


def solution():

    n = int(input())

    matrix = [list(map(int, input())) for _ in range(n)]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    res = []

    cnt = 0

    dq = collections.deque()

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                dq.append((i, j))

                while dq:
                    now = dq.popleft()
                    matrix[now[0]][now[1]] = 0
                    cnt += 1
                    for k in range(4):
                        y = now[0] + dy[k]
                        x = now[1] + dx[k]
                        if 0 <= y <= n - 1 and 0 <= x <= n - 1:
                            if matrix[y][x] == 1:
                                dq.append((y, x))

                res.append(cnt)
                cnt = 0

    print(len(res))
    for e in sorted(res):
        print(e)


solution()


# DFS 풀이와 같이 뽑고 0으로 처리하려고 했으나,
# 0으로 처리하지 않고 큐에 저장된 상태라면
# 해당 위치는 다른 위치에서도 또 다시 접근할 수 있으므로 방문하자마자 바로 0으로 할당해줘야한다.


