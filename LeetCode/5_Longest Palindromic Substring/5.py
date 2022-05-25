# 가장 긴 팰린드롬 부분 문자열

# s = "cbbd"
# s = "babad"
# s = "123454321"
s = "123456765"


def f():
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 해당 사항이 없을때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


print(f())


a = 'abc'

print(a[2:1])

b = a[2:1]
print(b)

c = a[1:2]
print(c)

d = a[1:2]
print(f'd: {d}')