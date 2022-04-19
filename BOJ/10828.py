import sys

input = sys.stdin.readline
n = int(input())

stack = []
for i in range(n):
    c = input().strip()
    if "push " in c:
        c = c.split()
        stack.append(c[1])
    elif c == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif c == "size":
        print(len(stack))
    elif c == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif c == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
