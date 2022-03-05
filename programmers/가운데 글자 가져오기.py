# 내 풀이.
def solution(s):

    if len(s) % 2:
        answer = s[len(s) // 2]
    else:
        answer = s[(len(s) // 2) - 1:len(s) // 2 + 1]

    print(str[(len(str)-1)//2:len(str)//2+1])
    return answer

s1 = 'abcde'
s2 = 'qwer'
s3 = 'qw'
s4 = 'q'
# print(solution(s1))
# print(solution(s2))
# print(solution(s3))
# print(solution(s4))


# 다른사람 풀이

# 풀이 1.
def solution2(s):
    return s[(len(s) - 1) // 2:len(s) // 2 + 1]


print(solution2(s1))
print(solution2(s2))
print(solution2(s3))
print(solution2(s4))