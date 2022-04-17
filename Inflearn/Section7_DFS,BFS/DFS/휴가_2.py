# 시작일을 1부터 시작한 경우


def solution():

    n = int(input())

    t = [0]
    p = [0]
    for _ in range(n):
        a, b = map(int, input().split())
        t.append(a)
        p.append(b)

    biggest = -2147000000

    def dfs(day, p_acc):
        nonlocal biggest

        if day == n + 1:
            if p_acc > biggest:
                biggest = p_acc
            return
        else:
            if day + t[day] <= n + 1:
                dfs(day + t[day], p_acc + p[day])
            dfs(day + 1, p_acc)
            return

    dfs(1, 0)

    print(biggest)


solution()

