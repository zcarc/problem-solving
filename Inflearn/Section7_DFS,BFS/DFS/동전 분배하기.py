def solution():
    n = int(input())

    coins = []
    for _ in range(n):
        coins.append(int(input()))

    money = [0] * 3
    smallest = 2147000000

    def dfs(level):
        nonlocal smallest

        if level == n:
            subtraction = max(money) - min(money)
            if subtraction < smallest:
                tmp = set()
                for i in range(3):
                    tmp.add(money[i])
                if len(tmp) == 3:
                    smallest = subtraction
        else:
            for i in range(3):
                money[i] = money[i] + coins[level]
                dfs(level + 1)
                money[i] = money[i] - coins[level]

    dfs(0)

    print(smallest)


solution()