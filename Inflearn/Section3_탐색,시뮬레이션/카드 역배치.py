def solution():

    arr = list(range(1, 21))

    for _ in range(10):
        a, b = map(int, input().split())

        tmp = arr[a - 1:b][::-1]

        for i in range(len(tmp)):
            arr[i + (a - 1)] = tmp[i]

    return arr


print(*solution())