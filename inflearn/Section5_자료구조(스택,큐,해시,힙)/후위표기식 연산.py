def solution():

    exp = input()

    stack = []

    for e in exp:

        if e.isdecimal():
            stack.append(e)

        else:
            b = int(stack.pop())
            a = int(stack.pop())

            if e == '+':
                stack.append(a + b)
            elif e == '-':
                stack.append(a - b)
            elif e == '*':
                stack.append(a * b)
            else:
                stack.append(a / b)

    return stack.pop()


print(solution())