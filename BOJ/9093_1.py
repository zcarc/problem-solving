import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    s = input()
    ls = s.split()
    lt = []
    for j in ls:
        lt.append(j[::-1])

    for k in lt:
        print(k, end=' ')
    print()
