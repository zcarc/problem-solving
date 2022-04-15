def solution():

    arr = list(range(21))

    for _ in range(10):
        start, end = map(int, input().split())

        for i in range((end - start + 1) // 2):
            arr[start + i], arr[end - i] = arr[end - i], arr[start + i]

    return arr[1:]


print(*solution())