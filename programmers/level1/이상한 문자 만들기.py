# 2022.02.11

# 내 풀이
def solution(s):

    arr = s.split(' ')
    for i in range(len(arr)):
        tmp = ''
        for j in range(len(arr[i])):
            if j % 2 == 0:
                tmp += arr[i][j].upper()
            else:
                tmp += arr[i][j].lower()

        arr[i] = tmp

    answer = ' '.join(arr)
    return answer


s1 = "try   hello       world"
# s = "t  he     wor"
# print(solution(s1))


# 다른사람 풀이

# 풀이 1.
def s(s):
    answer = ''
    cnt = 0

    for i in range(len(s)):
        cnt += 1
        if s[i] == ' ':
            cnt = 0
            answer += ' '
        elif cnt % 2 == 1:
            answer += s[i].upper()
        elif cnt % 2 == 0:
            answer += s[i].lower()

    return answer


print(s(s1))