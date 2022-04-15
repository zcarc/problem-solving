def solution():

    parentheses = input()

    stack = [parentheses[0]]

    cnt = 1
    res = 0

    for p in parentheses[1:]:

        if p == ')':
            cnt -= 1

            if stack[-1] == '(':
                res += cnt
            elif stack[-1] == ')':
                res += 1

            stack.append(p)

        elif p == '(':
            cnt += 1
            stack.append(p)

    return res


print(solution())
