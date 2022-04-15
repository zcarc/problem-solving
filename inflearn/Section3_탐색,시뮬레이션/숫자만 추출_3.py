def get_divisor_count(n):

    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1

    return cnt


def solution():

    s = input()

    digit = ''
    for c in s:
        if 48 <= ord(c) <= 57:
            digit += c

    digit = int(digit)
    divisor_count = get_divisor_count(digit)

    print(digit)
    print(divisor_count)


solution()
