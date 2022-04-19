n = int(input())

l = []

for _ in range(n):
    t = int(input())
    l.append(t)

for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            tmp = l[i]
            l[i] = l[j]
            l[j] = tmp

for i in l:
    print(i)
