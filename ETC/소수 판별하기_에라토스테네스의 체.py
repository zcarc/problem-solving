def solution(n):

    arr = [True] * (n + 1)

    for i in range(2, int(n ** (1/2)) + 1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                if j % i == 0:
                    arr[j] = False

    return [i for i in range(2, n + 1) if arr[i]]


print(solution(10))