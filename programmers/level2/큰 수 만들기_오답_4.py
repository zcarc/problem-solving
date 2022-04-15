from collections import deque


def solution(number, k):

    n = len(number)

    stack = []

    number = deque(number)

    for i in range(len(number)):
        if len(stack) == n - k:
            break

        if number and len(stack) + len(number) == n - k:
            stack.append(number.popleft())
        else:
            while stack and stack[-1] < number[0] and len(stack) + len(number) > n - k:
                stack.pop()
            stack.append(number.popleft())

    return ''.join(stack)


# print(solution("1231234", 3))
print(solution("87654321", 3))



