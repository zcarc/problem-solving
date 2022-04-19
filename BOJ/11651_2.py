import sys

input = sys.stdin.readline
n = int(input())

l = []
for i in range(n):
    x, y = map(int, input().split())
    l.append([x, y])

l.sort(key=lambda x: (x[1], x[0]))

for x, y in l:
    print(x, y)
