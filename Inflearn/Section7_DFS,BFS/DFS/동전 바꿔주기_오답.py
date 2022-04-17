def solution():

    t = int(input())
    k = int(input())

    amounts = []
    numbers = []
    for _ in range(k):
        a, b = map(int, input().split())
        amounts.append(a)
        numbers.append(b)

    cnt = 0

    def dfs(acc):
        nonlocal cnt
        print(numbers)

        if acc > t:
            return

        if acc == t:
            cnt += 1
            return
        else:
            for i in range(k):
                if numbers[i] <= 0:
                    continue

                numbers[i] -= 1
                dfs(acc + amounts[i])
                numbers[i] += 1
            return

    dfs(0)

    print(cnt)


solution()

