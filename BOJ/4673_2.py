a = list(range(1, 10_001))

l = []
for i in a:
    for j in str(i):
        i += int(j)
    if i < 10_001:
        l.append(i)


set_l = set(l)

for i in set_l:
    a.remove(i)

for i in a:
    print(i)