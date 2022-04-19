l = list()
for i in range(9):
    a = int(input())
    l.append(a)

max = l[0]
idx = 0
for i in l:
    if max < i:
        max = i
        idx = l.index(i)

print(max, idx+1, sep='\n')

