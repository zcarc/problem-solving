def solution():

    n, m = map(int, input().split())

    values = []
    times = []
    for _ in range(n):
        value, time = map(int, input().split())
        values.append(value)
        times.append(time)

    biggest = -2147000000

    def dfs(level, acc, time_acc):
        nonlocal biggest

        if time_acc > m:
            return

        if level == n:
            if acc > biggest:
                biggest = acc
            return
        else:
            dfs(level + 1, acc + values[level], time_acc + times[level])
            dfs(level + 1, acc, time_acc)
            return

    dfs(0, 0, 0)

    print(biggest)


solution()

