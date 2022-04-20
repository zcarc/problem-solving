def solution(n):

    s = ""
    while n != 0:
        n, r = divmod(n, 3)
        s += str(r)

    n = int(s)

    decimal = 0
    for i, number in enumerate(str(n)[::-1]):
        decimal += int(number) * (3 ** i)

    return decimal


print(solution(45))


