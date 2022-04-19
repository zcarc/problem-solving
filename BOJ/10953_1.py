import sys
input = sys.stdin.readline
t = int(input())

l = []
for i in range(t):
    k = input().strip()
    l.append(k)

for i in l:
    a, b = map(int, i.split(','))
    print(a + b)
