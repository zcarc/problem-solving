import sys
input = sys.stdin.readline
n = int(input())

l = []
for i in range(n):
    s = input().strip()
    l.append(s)

l = list(set(l))

l.sort(key=lambda x: (len(x), x))

for i in l:
    print(i)
