n, k = map(int, input().split())


def solution(n, k):

    arr = list(map(int, input().split()))

    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for m in range(j + 1, len(arr)):
                result.append(arr[i] + arr[j] + arr[m])

    result = sorted(set(result), reverse=True)

    return result[k - 1]


print(solution(n, k))