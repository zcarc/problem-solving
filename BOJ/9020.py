def getPrimes(n):
    arr = [False] * (n + 1)
    arr[0] = arr[1] = True

    for i in range(2, int(n ** (1 / 2)) + 1):
        if arr[i] == True:
            continue
        for j in range(i * i, len(arr), i):
            if j % i == 0:
                arr[j] = True

    return arr


arr = getPrimes(10000)


t = int(input())

for _ in range(t):
    n = int(input())

    p = n // 2
    q = n // 2

    while True:
        if arr[p] == False and arr[q] == False:
            print(p, q)
            break
        p -= 1
        q += 1
