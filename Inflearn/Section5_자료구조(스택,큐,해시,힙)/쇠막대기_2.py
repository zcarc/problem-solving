def solution():

    parentheses = input()

    stack = []

    res = 0

    for i, p in enumerate(parentheses):

        if p == ')':
            if parentheses[i - 1] == '(':
                stack.pop()
                res += len(stack)

            elif parentheses[i - 1] == ')':
                stack.pop()
                res += 1

        elif p == '(':
            stack.append(p)

    return res


print(solution())
