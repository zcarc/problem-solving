def solution(n):

    s = ''
    while n != 0:
        n, r = divmod(n, 3)
        if r == 0:
            s += '4'
            n -= 1
        else:
            s += str(r)

    return s[::-1]


print(solution(3))
print(solution(6))
print(solution(9))
print(solution(10))


# 참고
# https://yabmoons.tistory.com/692?category=946152