def solution():

    n = int(input())
    g = list(map(int, input().split()))
    s = sum(g)
    res = set()

    def dfs(level, acc):
        nonlocal res

        if level == n:
            if 0 < acc <= s:
                res.add(acc)
        else:
            dfs(level + 1, acc + g[level])
            dfs(level + 1, acc - g[level])
            dfs(level + 1, acc)

    dfs(0, 0)

    print(s - len(res))


solution()