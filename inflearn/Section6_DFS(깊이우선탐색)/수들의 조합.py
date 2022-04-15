def solution():

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())

    cnt = 0
    tmp = []

    def dfs(level, start):
        nonlocal cnt

        if level == k:
            if sum(tmp) % m == 0:
                cnt += 1
            return
        else:
            for i in range(start, n + 1):
                tmp.append(arr[i - 1])
                dfs(level + 1, i + 1)
                tmp.pop()
            return

    dfs(0, 1)

    print(cnt)


solution()
