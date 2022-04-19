a = int(input())
h = 0
for i in range(1, a+1):
    if i < 100:
        h += 1
    else:
        l = list(map(int, str(i)))
        if l[0] - l[1] == l[1] - l[2]:
            h += 1

print(h)