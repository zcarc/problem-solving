# n진수에서 10진수로 변환하는 알고리즘
def to_decimal(n, radix):
    decimal = 0
    for index, number in enumerate(str(n)[::-1]):
        decimal += int(number) * (radix ** index)

    return decimal


print(to_decimal(111010100, 2))


# 10진수에서 n진수로 변환하는 알고리즘
def to_n_radix(n, radix):
    n_radix = ''
    while n > 0:
        n, r = divmod(n, radix)
        n_radix += str(r)

    return int(n_radix[::-1])


n = 10
radix = 2
print(to_n_radix(n, radix))

# n진수에서 n진수로 변환하는 알고리즘
# n진수에서 10진수로 변환하고 다시 n진수로 변환한다.
# ex) 16진수에서 2진수로 변환
result = to_n_radix(int('c', 16), 2)
print(result)