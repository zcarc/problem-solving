def solution():

    l = int(input())

    arr = list(map(int, input().split()))

    m = int(input())

    arr.sort()

    idx_smallest = 0
    idx_biggest = l - 1

    for _ in range(m):
        if idx_smallest == idx_biggest:
            arr.sort()
            idx_smallest = 0
            idx_biggest = l - 1

        if arr[idx_biggest - 1] <= arr[idx_biggest]:
            arr[idx_biggest] -= 1
        else:
            idx_biggest -= 1
            arr[idx_biggest] -= 1

        if arr[idx_smallest + 1] >= arr[idx_smallest]:
            arr[idx_smallest] += 1
        else:
            idx_smallest += 1
            arr[idx_smallest] += 1

    arr.sort()
    idx_smallest = 0
    idx_biggest = l - 1

    return arr[idx_biggest] - arr[idx_smallest]


solution()

