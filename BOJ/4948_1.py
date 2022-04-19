n = -1
while True:
    n = int(input())
    if n == 0:
        break

    l = [False] * ((n * 2) + 1)
    l[0] = l[1] = True

    for i in range(2, int((n * 2) ** (1/2)) + 1):
        if l[i] == True:
            continue
        for j in range(i * i, len(l), i):
            if j % i == 0:
                l[j] = True

    cnt = 0
    for i in range(n + 1, (n * 2) + 1):
        if l[i] == False:
            cnt += 1

    print(cnt)

