import sys
input = sys.stdin.readline
n = int(input())

l = []
for i in range(n):
    x, y = map(int, input().split())
    l.append([y, x])

l = sorted(l)

for y, x in l:
    print(x, y)