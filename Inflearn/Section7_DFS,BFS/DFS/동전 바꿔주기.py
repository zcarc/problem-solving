def solution():
    t = int(input())
    k = int(input())

    coin_values = []
    coin_numbers = []
    for _ in range(k):
        a, b = map(int, input().split())
        coin_values.append(a)
        coin_numbers.append(b)

    cnt = 0

    def dfs(level, acc):
        nonlocal cnt

        if acc > t:
            return

        if level == k:
            if acc == t:
                cnt += 1
            return
        else:
            for i in range(coin_numbers[level] + 1):
                dfs(level + 1, acc + (i * coin_values[level]))
            return

    dfs(0, 0)

    print(cnt)


solution()


# 정답