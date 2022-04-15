def solution():

    n = int(input())

    arr = [0] + list(map(int, input().split()))

    sequence = [0] * n

    for i in range(1, n + 1):
        for j in range(n):
            if arr[i] == 0 and sequence[j] == 0:
                sequence[j] = i
                break

            elif sequence[j] == 0:
                arr[i] -= 1

    return ' '.join(map(str, sequence))


print(solution())

