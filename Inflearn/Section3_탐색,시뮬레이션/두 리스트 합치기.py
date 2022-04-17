def solution():

    matrix = []
    for _ in range(2):
        n = int(input())
        tmp = list(map(int, input().split()))
        matrix.append(tmp)

    arr1 = matrix[0]
    arr2 = matrix[1]

    p1 = 0
    p2 = 0

    result = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] > arr2[p2]:
            result.append(arr2[p2])
            p2 += 1
        else:
            result.append(arr1[p1])
            p1 += 1

    if p1 >= len(arr1):
        for i in range(p2, len(arr2)):
            result.append(arr2[i])

    if p2 >= len(arr2):
        for i in range(p1, len(arr1)):
            result.append(arr1[i])

    return ' '.join(str(e) for e in result)


print(solution())
