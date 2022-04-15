
def solution(s):

    stack = []

    for x in s:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if not stack:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


# s = '()()'
# s = '(())()'
# s = ')()('
# s = '(()('
s = '(())(()))'
print(solution(s))