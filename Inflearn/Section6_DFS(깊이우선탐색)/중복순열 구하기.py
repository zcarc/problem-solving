def solution():

    n, m = map(int, input().split())

    arrival = [0] * m

    cnt = 0

    def dfs(level):
        nonlocal cnt

        if level == m:
            for v in arrival:
                print(v, end=' ')
            cnt += 1
            print()
        else:
            for i in range(1, n + 1):
                arrival[level] = i
                dfs(level + 1)

    dfs(0)

    print(cnt)


solution()