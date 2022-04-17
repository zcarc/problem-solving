def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# 보통은 첫번째 인수에 더 큰 수가 오지만 두번째 인수에 더 큰 수가 와도 동일하게 동작한다.
# 즉, a, b의 순서가 바뀌어도 답은 같다.
print(gcd(162, 192))


def lcd(a, b):
    return a * b // gcd(a, b)


print(lcd(162, 192))


# gcd 호출 예시

# A.
# 1. call gcd(a = 10,  b = 20)
# 2. return gcd(20, 10 % 20 (= 10))
# 3. call gcd(20, 10)
# 4. if a(20) % b(10) == 0:
#        return b (= 10)

# B.
# 1. call gcd(162, 192)
# 2. return gcd(192, 162 % 192 (= 162))
# 3. call gcd(192, 162)
# 4. return gcd(162, 192 % 162 (= 30))
# 5. call gcd(162, 30)
# 6. return gcd(30, 162 % 30 (= 12))
# 5. call gcd(30, 12)
# 6. return gcd(12, 30 % 12 (= 6))
# 7. call gcd(12, 6)
# 8. if a(12) % b(6) == 0:
#        return b (= 6)
