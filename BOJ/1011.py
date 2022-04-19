t = int(input())

for _ in range(t):
    X, Y = list(map(int, input().split()))
    distance = Y - X
    maximum = int(distance ** (1/2))

    if maximum == distance ** (1/2):
        print(maximum * 2 - 1)

    elif distance <= maximum * maximum + maximum:
        print(maximum * 2)

    else:
        print(maximum * 2 + 1)
