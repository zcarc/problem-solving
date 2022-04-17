

def solution():

    c, n = map(int, input().split())

    arr = []
    for _ in range(n):
        arr.append(int(input()))

    total = sum(arr)

    res = -2147000000

    def dfs(level, acc, total_acc):
        nonlocal res

        if acc + (total - total_acc) < res:
            return

        if acc > c:
            return

        if level == n:
            if acc > res:
                res = acc
        else:
            dfs(level + 1, acc + arr[level], acc + arr[level])
            dfs(level + 1, acc, acc + arr[level])

    dfs(0, 0, 0)

    return res


print(solution())

