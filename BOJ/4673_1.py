a = set(range(1, 10_001))
s = set()

for i in a:
    for j in str(i):
        i += int(j)
    if i < 10_001:
        s.add(i)

difference = a-s

for i in sorted(difference):
    print(i)