n, m = map(int, input().split())


def solution(n, m):

    arr = [0] * (n + m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            arr[i + j] += 1

    max_value = -2147000000
    for i in range(1, n + m + 1):
        if arr[i] > max_value:
            max_value = arr[i]

    for i in range(1, n + m + 1):
        if arr[i] == max_value:
            print(i, end=' ')


solution(n, m)


