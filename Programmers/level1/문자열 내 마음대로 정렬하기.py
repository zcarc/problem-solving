# 2022.02.13
from typing import List


# 내 풀이 1.
def solution(strings: List[str], n):
    strings.sort(key=lambda x: (x[n], x))
    return strings


# 내 풀이 2.
def solution2(strings, n):

    answer = []
    sorted_min = []

    for i in strings:
        sorted_min.append(i[n])

    sorted_min.sort()
    strings.sort()

    for i in range(len(sorted_min)):
        for j in range(len(strings)):
            if strings[j] and sorted_min[i] == strings[j][n]:
                answer.append(strings[j])
                strings[j] = []

    return answer


# 다른사람 풀이

# 풀이 1. (기존 코드 변경해서 풀이)
def solution3(strings: List[str], n):

    tmp = []
    for c in strings:
        tmp.append(c[n] + c)

    tmp.sort()

    answer = []
    for c in tmp:
        answer.append(c[1:])

    return answer


strings = ["sun", "bed", "car"]
n = 1
strings2 = ["abce", "abcd", "cdx"]
n2 = 2
