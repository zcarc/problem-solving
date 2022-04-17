def solution():

    n = int(input())

    arr = list(map(int, input().split()))

    sequence = [0] * n

    for i in range(n):
        for j in range(n):
            if arr[i] == 0 and sequence[j] == 0:
                sequence[j] = i + 1
                break

            elif sequence[j] == 0:
                arr[i] -= 1

    return ' '.join(map(str, sequence))


print(solution())

