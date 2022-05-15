def solution(w, h):

    def gcd(a, b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)

    g = gcd(w, h)

    return (w * h) - (w + h - g)


print(solution(8, 12))


# 이 문제는 "대각선이 지나는 단위정사각형"의 개수를 구하는 공식을 이용해서 풀어야한다.

# 직사각형의 각 변의 길이가 서로소가 아니면 대각선을 지날 때 중간에 교점을 지나서 대각선을 기준으로 평행하여 지날 수 있는 단위정사각형이 없는 경우가 있다.
# 서로소라면 대각선을 기준으로 지날 때, 단위 정사각형의 개수가 평행하면서 지나게 된다.

# 3 * 2는 서로소이고 대각선의 지나는 단위정사각형의 개수는 4개가 된다. (w + h - 1)
# 3 * 2가 6 * 4인 직사각형의 일부라면,
# 6 * 2 직사각형에서 3 * 2의 개수는 4개가 된다. (6, 2의 최대 공약수 = 2)
# b(3) * c(2) 사각형을 gcd(2)^2 개로 분할할 수 있다. (w = gcd * b, h = gcd * c)
# 대각선이 지나가는 b(3) * c(2) 사각형의 개수는 gcd(2)개이다.
# b(3), c(2)가 서로소이므로 b(3) * c(2) 사각형에서 "대각선이 지나가는 단위사각형"은 b(3) + c(2) - 1 이고,
# w * h 사각형을 전체적으로 보면
# ( gcd(2) * b(3) + gcd(2) * c(2) ) - gcd(2) 또는 w(6) + h (4) - gcd(2) 가 된다.

# 공식
# a(b+c-1) = ab+ac-a = m+n-a

# 서로소라는 것은 가로 * 세로의 최대 공약수가 1이라는 것이고,
# 서로소가 아니라는 것은 가로 * 세로의 최대 공약수가 2 이상을 의미한다.


# 참고
# https://hyojun.tistory.com/entry/Programmers-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-Java
# https://m.blog.naver.com/zzinuhelios/120024685950
# https://ashrock.kr/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95/
# https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-in-python
