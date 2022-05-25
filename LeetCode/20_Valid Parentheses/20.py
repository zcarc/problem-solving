def isValid(s) -> bool:
    stack = []
    table = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or stack.pop() != table[char]:
            return False

    return len(stack) == 0