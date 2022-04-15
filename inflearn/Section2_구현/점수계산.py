def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    answer = []
    cnt = 0
    for i in range(1, n):
        if arr[i - 1] == 0:
            cnt = 0
            answer.append(cnt)
        else:
            cnt += 1
            answer.append(cnt)

    if arr[-1] == 0:
        cnt = 0
        answer.append(cnt)
    else:
        cnt += 1
        answer.append(cnt)

    return sum(answer)


print(solution())