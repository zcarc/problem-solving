l = [int(input()) for _ in range(3)]
s = l[0] * l[1] * l[2]

for i in range(10):
    print(str(s).count(str(i)))