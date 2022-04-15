

def solution():

    c, n = map(int, input().split())

    arr = []
    for _ in range(n):
        arr.append(int(input()))

    res = -2147000000

    def dfs(level, acc):

        if acc > c:
            return

        if level == n:
            nonlocal res
            if acc > res:
                res = acc
        else:
            dfs(level + 1, acc + arr[level])
            dfs(level + 1, acc)

    dfs(0, 0)

    return res


print(solution())

