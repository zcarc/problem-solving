def solution():

    n, m = map(int, input().split())

    arrival = [0] * m

    cnt = 0

    def dfs(level, start):
        nonlocal cnt

        if level == m:
            for v in arrival:
                print(v, end=' ')
            cnt += 1
            print()
        else:
            for i in range(start, n + 1):
                arrival[level] = i
                dfs(level + 1, i + 1)

    dfs(0, 1)

    print(cnt)


solution()

