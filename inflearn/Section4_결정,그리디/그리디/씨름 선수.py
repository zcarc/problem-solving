def solution():

    n = int(input())

    arr = [tuple(map(int, input().split())) for _ in range(n)]

    arr.sort(reverse=True)

    cnt = n
    for i in range(n - 1):
        if arr[i]:
            for j in range(i + 1, n):
                if arr[j]:
                    if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
                        arr[j] = []
                        cnt -= 1

    return cnt


print(solution())
