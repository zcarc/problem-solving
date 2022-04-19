n = int(input())

l = []

for i in range(n):
    t = int(input())
    l.append(t)

l.sort()

for i in l:
    print(i)
