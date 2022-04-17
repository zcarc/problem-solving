import itertools


def solution():

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())

    cnt = 0
    for x in itertools.combinations(arr, k):
        if sum(x) % m == 0:
            cnt += 1

    print(cnt)


solution()
