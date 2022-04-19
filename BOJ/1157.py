a = input().upper()
setA = list(set(a))
b = []

for i in setA:
    cnt = a.count(i)
    b.append(cnt)

if b.count(max(b)) > 1:
    print('?')
else:
    idx = b.index(max(b))
    print(setA[idx])