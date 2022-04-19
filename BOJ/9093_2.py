import sys

input = sys.stdin.readline


def reverse_stack(s):
    s += " "
    stack = []
    for i in s:
        if i != " ":
            stack.append(i)
        else:
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')
    print()


n = int(input())

for i in range(n):
    s = input().rstrip()
    reverse_stack(s)
