# 2022.02.13

def solution(s):
    s = list(s)
    s.sort(reverse=True)


s = "bcdZefg"
print(solution(s))


# 다른사람 풀이

# 풀이 1.
def solution2(s):
    return ''.join(sorted(s, reverse=True))


# sorted() 함수는 문자열을 넣으면 리스트로 변환해서 정렬해준다.
# 리스트도 넣을 수 있다.
