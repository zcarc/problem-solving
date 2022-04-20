def solution(n):

    s = ""
    while n != 0:
        n, r = divmod(n, 3)
        s += str(r)

    return int(s, 3)
