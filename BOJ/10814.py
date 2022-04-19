import sys
input = sys.stdin.readline
n = int(input())

l = []
for i in range(n):
    x, y = input().split()
    l.append([x, y])

l.sort(key=lambda x: int(x[0]))

for x, y in l:
    print(x, y)
