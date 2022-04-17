def solution():

    n, m = map(int, input().split())

    arrival = [0] * m
    ch = [0] * (n + 1)
    cnt = 0

    def dfs(level):
        nonlocal cnt

        if level == m:
            for x in arrival:
                print(x, end=' ')
            print()
            cnt += 1
            return
        else:
            for i in range(1, n + 1):
                if ch[i] == 1:
                    continue
                arrival[level] = i
                ch[i] = 1
                dfs(level + 1)
                ch[i] = 0
            return

    dfs(0)

    print(cnt)


solution()