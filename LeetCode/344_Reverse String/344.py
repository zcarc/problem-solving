def reverse_string(s):
    return s[::-1]

s = ["h","e","l","l","o"]

# print(reverse_string(s))

# 이 문제에서는 반환하지 않고 해당 배열 내에서만 조작하면 되므로 따로 반환하지 않았다.

# 투포인터를 이용한 스왑
def reverseString(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


s2 = [1,2,3]
s2 = s2[::-1]

print(s2)