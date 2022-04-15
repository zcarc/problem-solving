n = int(input())
arr = list(map(int, input().split()))


# reverse 함수만 다른 방식으로 풀이
def reverse(n):

    result = 0
    while n != 0:
        r = n % 10
        n = n // 10
        result = result * 10 + r

    return result


def get_prime_arr(n):

    arr = [True] * (n + 1)

    for i in range(2, int(n ** (1/2))):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                if j % i == 0:
                    arr[j] = False

    return arr


def solution(n, arr):

    for i in range(n):
        arr[i] = reverse(arr[i])

    prime_arr = get_prime_arr(max(arr))

    for e in arr:
        if e >= 2:
            if prime_arr[e]:
                print(e, end=' ')


solution(n, arr)