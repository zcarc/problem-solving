n = int(input())

arr = [[0] * 2 for _ in range(n)]


for i in range(n):
    x, y = list(map(int, input().split()))
    arr[i][0] = x
    arr[i][1] = y


for i in range(n):
    rank = 1

    for j in range(n):
        if i == j:
            continue

        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1

    print(rank, end=" ")

