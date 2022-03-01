# 유요한 팰린드롬
# 125 Valid Palindrome

# 만약 짝수인 경우 반으로 나눠서 끝값하고 비교해보자
# 만약
# abba
#
# 이라는 문자열이 있다면
#
# 여기서 비교 대상은 0,1,2,3
# 4//2 = 2 이므로 2앞까지만 비교하면 된다.
#
# a[0] == a[-1] 같고
# a[1] == a[-2] 같다
# 둘다 같으므로 결국에는 이 문자열은 유요한 팰린드롬이 맞는문제이다.

# 그럶 만약에 짝수가 아니라 홀수인 경우면 어떻게하면 좋을지 생각해보면
# aabbcbbaa 라는 값이 있다면 123456789
# 9 // 2 = 4라는 값이 되니까 4 앞까지면 3번째 인덱스를 기준으로 정한다는 이야기다
# 어차피 중간값은 비교할 대상이 없기 때문에 가운데 하나는 그냥 놔준다.
import collections

string = "A man, a plan, a canal: Panama"

# 내가 쓴 풀이
def valid(s):
    l = []
    for i in s:
        if i.isalnum():
            l.append(i)

    for i in range(len(l) // 2):
        if l[i].upper() != l[len(l) - 1 - i].upper():
            return False
    return True


# 풀이 1
def a1(str: str):
    strs = collections.deque()
    for i in str:
        if i.isalnum():
            strs.append(i.lower())

    print(f'strs: {strs}')

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


# print(a1(string))

import re


def a2(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

# print(a2('Ab$51C41DSe63&%(^dkf'))


l = [1,2,3,4,5,6]
print(l)

print(l.pop(0))

print(l)
