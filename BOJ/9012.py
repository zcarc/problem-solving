import sys
input = sys.stdin.readline
n = int(input())


def check(str):
    stack = []

    for j in str:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                return False

    return len(stack) == 0


for i in range(n):
    c = input().strip()

    if check(c):
        print('YES')
    else:
        print('NO')
