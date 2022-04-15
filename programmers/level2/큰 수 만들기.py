def solution(number, k):

    stack = []

    for n in number:
        while k > 0 and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)

    return ''.join(stack[:len(number) - k])


number = "1231234"
k = 3
print(solution(number, k))

# number = "4177252841"
# k = 4
# print(solution(number, k))

# number = "9876"
# k = 2
# print(solution(number, k))


# 참고:
# https://velog.io/@soo5717/프로그래머스-큰-수-만들기-파이썬
