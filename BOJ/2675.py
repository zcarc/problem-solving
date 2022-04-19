a = int(input())

for i in range(a):
    a = input().split(' ')
    r = a[0]
    s = a[1]

    for j in s:
        print(j*int(r), end='')
    print()