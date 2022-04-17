def solution():

    l = int(input())

    arr = list(map(int, input().split()))

    m = int(input())

    arr.sort()

    smallest = 0
    biggest = l - 1

    for _ in range(m):
        arr[smallest] += 1
        arr[biggest] -= 1
        arr.sort()

    return arr[biggest] - arr[smallest]


print(solution())

