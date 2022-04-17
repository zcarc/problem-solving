n, k = map(int, input().split())


def solution(n, k):

    arr = []
    for i in range(1, n + 1):
        if n % i == 0:
            arr.append(i)

    if k > len(arr):
        return -1

    return arr[k - 1]


# n, k = 6, 3
print(solution(n, k))