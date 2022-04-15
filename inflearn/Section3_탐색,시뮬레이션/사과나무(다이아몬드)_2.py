def solution():

    n = int(input())

    arr = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        arr.append(tmp)

    result = 0

    start = end = n // 2
    for i in range(n):
        for j in range(start, end + 1):
            result += arr[i][j]

        if i < n // 2:
            start -= 1
            end += 1
        elif i >= n // 2:
            start += 1
            end -= 1

    return result


print(solution())
