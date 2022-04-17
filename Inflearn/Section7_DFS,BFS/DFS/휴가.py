# 시작일을 0부터 시작한 경우


def solution():

    n = int(input())

    t = []
    p = []
    for _ in range(n):
        a, b = map(int, input().split())
        t.append(a)
        p.append(b)

    biggest = -2147000000

    def dfs(level, p_acc):
        nonlocal biggest

        if level > n:
            return

        if level == n:
            if p_acc > biggest:
                biggest = p_acc
            return
        else:
            dfs(level + t[level], p_acc + p[level])
            dfs(level + 1, p_acc)
            return

    dfs(0, 0)

    print(biggest)


solution()

