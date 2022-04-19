import sys

input = sys.stdin.readline
n = int(input())

l = []
for i in range(n):
    s = input().strip()
    l.append(s)

l.sort(key=lambda x: (len(x), x))

tmp = []
for i in l:
    if i not in tmp:
        tmp.append(i)

for i in tmp:
    print(i)
