# 2022.02.11
from string import ascii_lowercase, ascii_uppercase


# 내 풀이
def solution(s, n):
    answer = ''

    for c in s:
        if c.islower():
            if ascii_lowercase.index(c) + n > len(ascii_lowercase) - 1:
                index = (ascii_lowercase.index(c) + n) - (len(ascii_lowercase) - 1)
                answer += ascii_lowercase[index - 1]
            else:
                answer += ascii_lowercase[ascii_lowercase.index(c) + n]

        elif c.isupper():
            if ascii_uppercase.index(c) + n > len(ascii_uppercase) - 1:
                index = (ascii_uppercase.index(c) + n) - (len(ascii_uppercase) - 1)
                answer += ascii_uppercase[index - 1]
            else:
                answer += ascii_uppercase[ascii_uppercase.index(c) + n]

        else:
            answer += ' '

    return answer


# s = 'AB'
# n = 1
s = 'a B z'
n = 4
print(solution(s, n))


# 다른사람 풀이

# 풀이 1.
def solution2(s: str, n: int):

    answer = ''

    for c in s:
        if c.islower():
            answer += chr((ord(c) - ord('a') + n) % 26 + ord('a'))

        elif c.isupper():
            answer += chr((ord(c) - ord('A') + n) % 26 + ord('A'))

        else:
            answer += ' '

    return answer


print(solution2(s, n))


# 유니코드로 푼 문제는
# 26으로 나눈 나머지를 구하는 연산이 들어가는데
# 이렇게 하는 이유는 0 ~ 25까지의 값이 나와야하기 때문이다.
# c가 'Z' 이고 n이 0 일 때,
# ord(c) - ord('A') + n = 25 가 되고
# 이 값을 26으로 나눈 나머지는 25가 된다
# 그래서 그 값을 다시 ord('A') 에 더하면 90 이 되므로 처음 입력값과 같아진다.
#
# 만약 여기서 c는 'Z' 이고 n은 1 이라면,
# ord(c) - ord('A') + n = 26 이 되고
# 26 % 26 = 0 이 되고
# 이 값을 ord('A')에 더하면 65가 되어 더해지는 값이 0이 되어 답은 'A'가 된다.
#
# 마지막 연산인 ord('A')(65)에 더할 때, 0 ~ 25 이내의 값이 나와야 대문자 알파벳 A ~ Z 까지만 찾을 수 있다.
#
# 길이는 26이지만 인덱스가 0 ~ 25이므로 Z + 1을 한다면 인덱스는 0이 되어야한다.






