# 2022.02.11

# 내 풀이
def solution(s):
    return int(s)


# 다른사람 풀이

# 풀이 1. (기존풀이에서 문자열 '+' 처리하는 부분을 추가해서 풀이)
def solution2(s):

    answer = 0

    for index, number in enumerate(s[::-1]):

        if number == '-':
            answer *= -1

        elif number == '+':
            continue

        else:
            answer += int(number) * (10 ** index)

    return answer


s = '+3019'
print(solution2(s), type(solution2(s)))


# 문자열을 뒤집어서 반복하는 이유는
# 현재 숫자(number) + 10의 제곱 i을 해서
# 일의 자리부터 더해나가기 위해서이다.