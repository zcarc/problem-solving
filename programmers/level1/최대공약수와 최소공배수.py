# 2022.02.10
import math


# 내 풀이
def solution(n, m):
    answer = []

    def gcd(n, m):
        res = 0
        for i in range(1, min(n, m) + 1):
            if n % i == 0 and m % i == 0:
                res = i

        return res

    def lcm(n, m):
        res = 0
        for i in range(n * m, max(n, m) - 1, -1):
            if i % n == 0 and i % m == 0:
                res = i

        return res

    answer.append(gcd(n, m))
    answer.append(lcm(n, m))

    return answer


# math 함수로 풀이
# math.lcm(n, m) 함수는 3.9 버전 이상부터 지원
def s(n, m):
    return [math.gcd(n, m), n * m // math.gcd(n, m)]


# 유클리드 호제법 반복문
def s2(n, m):

    def gcd(n, m):
        while n != 0:
            r = m % n
            m = n
            n = r

        return m

    def lcm(n, m):
        return n * m // gcd(n, m)

    return [gcd(n, m), lcm(n, m)]


# 유클리드 호제법 재귀
def s3(n, m):

    def gcd(n, m):
        if n == 0:
            return m
        r = m % n
        return gcd(r, n)

    def lcm(n, m):
        return n * m // gcd(n, m)

    return [gcd(n, m), lcm(n, m)]