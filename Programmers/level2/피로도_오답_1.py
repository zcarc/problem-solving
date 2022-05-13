def solution(k, dungeons):
    dungeons.sort()

    cnt = 0
    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            k -= dungeons[i][0]
            cnt += 1

    return cnt


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
