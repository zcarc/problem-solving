def solution():

    arr = []
    for _ in range(2):
        n = int(input())
        tmp = list(map(int, input().split()))
        arr += tmp

    arr.sort()

    return ' '.join(map(str, arr))


print(solution())
