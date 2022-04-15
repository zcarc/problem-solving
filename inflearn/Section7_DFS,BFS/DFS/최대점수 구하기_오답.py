def solution():

    n, m = map(int, input().split())

    pairs = []
    for _ in range(n):
        a, b = map(int, input().split())
        pairs.append((a, b))

    biggest = -2147000000

    def dfs(start, acc, time_acc):
        nonlocal biggest

        if time_acc == m:
            if acc > biggest:
                biggest = acc
            return
        else:
            for i in range(start, n + 1):
                dfs(i + 1, acc + pairs[i - 1][0], time_acc + pairs[i - 1][1])
            return

    dfs(0, 0, 0)

    print(biggest)


solution()

