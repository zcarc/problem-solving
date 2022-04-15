def solution():

    n = int(input())

    max_value = -21470000

    for _ in range(n):
        a, b, c = map(int, input().split())

        money = 0
        if a == b == c:
            money = 10000 + a * 1000
        elif a == b or a == c:
            money = 1000 + a * 100
        elif b == c:
            money = 1000 + b * 100
        else:
            money = max(a, b, c) * 100

        if money > max_value:
            max_value = money

    return max_value


print(solution())