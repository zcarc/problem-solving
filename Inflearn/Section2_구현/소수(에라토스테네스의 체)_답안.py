n = int(input())


def solution(n):

    arr = [0] * (n + 1)

    cnt = 0
    for i in range(2, n + 1):
        if arr[i] == 0:
            cnt += 1
            for j in range(i, n + 1, i):
                if arr[j] == 0:
                    arr[j] = 1

    return cnt


print(solution(n))