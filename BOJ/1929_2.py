a, b = list(map(int, input().split()))

l = [False] * (b + 1)


# Sieve of Eratosthenes
def getPrimes(arr):
    arr[0] = arr[1] = True

    for i in range(2, int(len(arr) ** (1/2)) + 1):
        if arr[i] == True:
            continue

        for j in range(i * i, len(arr), i):
            if j % i == 0:
                arr[j] = True

    return arr


arr = getPrimes(l)

for i in range(a, len(arr)):
    if arr[i] == False:
        print(i)
