a = input()
b = a.split()

c = []
for i in b:
    c.append(i[::-1])

d = [int(i) for i in c]

print(max(d))