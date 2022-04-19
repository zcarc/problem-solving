a = int(input())

for i in range(a):
    a = input()
    s = 0
    c = 0
    for j in a:
        if j == 'O':
            c += 1
            s += c
        else:
            c = 0
    print(s)