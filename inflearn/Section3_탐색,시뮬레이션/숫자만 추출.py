def get_divisor_count(n):

    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1

    return cnt


def solution():

    s = input()

    decimal = 0
    for c in s:
        if c.isdecimal():
            decimal = decimal * 10 + int(c)

    divisor_count = get_divisor_count(decimal)

    print(decimal)
    print(divisor_count)


solution()
