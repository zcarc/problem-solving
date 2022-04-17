def solution():

    exp = input()

    stack = []

    res = ''
    for e in exp:
        if 48 <= ord(e) <= 57:
            res += e
        else:
            if stack:
                if e == '+' or e == '-':
                    if stack[-1] == '(':
                        stack.append(e)
                    else:
                        while stack and (stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '*' or stack[-1] == '/'):
                            res += stack.pop()
                        stack.append(e)

                elif e == '*' or e == '/':
                    if stack[-1] == '(':
                        stack.append(e)
                    elif stack[-1] == '+' or stack[-1] == '-':
                        stack.append(e)
                    elif stack[-1] == '*' or stack[-1] == '/':
                        while stack and (stack[-1] == '*' or stack[-1] == '/'):
                            res += stack.pop()
                        stack.append(e)

                elif e == '(':
                    stack.append(e)

                elif e == ')':
                    while stack and stack[-1] != '(':
                        res += stack.pop()
                    stack.pop()

            else:
                stack.append(e)

    while stack:
        res += stack.pop()

    return res


print(solution())