a, b = list(map(int, input().split()))


for i in range(a, b + 1):
    if i == 1:
        continue

    for j in range(2, int(i ** (1/2)) + 1):
        if i % j == 0:
            break
    else:
        print(i)
