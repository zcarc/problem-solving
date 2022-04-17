def solution():

    n = int(input())

    arr = list(map(int, input().split()))

    arr = arr[::-1]

    sequence = []
    for i in range(len(arr)):
        sequence.insert(arr[i], n - i)

    return ' '.join(map(str, sequence))


print(solution())

