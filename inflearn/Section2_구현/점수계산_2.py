def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    sum_cnt = 0

    for e in arr:
        if e == 1:
            cnt += 1
            sum_cnt += cnt
        else:
            cnt = 0

    return sum_cnt


print(solution())