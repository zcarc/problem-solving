def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# a, b의 순서가 바뀌어도 답은 같다.
print(gcd(192, 162))


# lcd (개인적으로 추가함)
def lcd(a, b):
    return a * b // gcd(a, b)


print(lcd(192, 162))
