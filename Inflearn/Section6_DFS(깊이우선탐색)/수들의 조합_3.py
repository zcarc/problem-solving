def solution():

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())

    cnt = 0

    def dfs(level, start, acc):
        nonlocal cnt

        if level == k:
            if acc % m == 0:
                cnt += 1
            return
        else:
            for i in range(start, n):
                dfs(level + 1, i + 1, acc + arr[i])
            return

    dfs(0, 0, 0)

    print(cnt)


solution()
