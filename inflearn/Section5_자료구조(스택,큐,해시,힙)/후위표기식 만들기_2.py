def solution():

    exp = input()

    stack = []

    res = ''
    for e in exp:
        if e.isdecimal():
            res += e
        else:
            if e == '+' or e == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(e)

            elif e == '*' or e == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    res += stack.pop()
                stack.append(e)

            elif e == '(':
                stack.append(e)

            elif e == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()

    while stack:
        res += stack.pop()

    return res


print(solution())