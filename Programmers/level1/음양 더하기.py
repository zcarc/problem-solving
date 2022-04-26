def solution(absolutes, signs):
    length = len(absolutes)

    total = 0
    for i in range(length):
        if signs[i] is False:
            total += -1 * absolutes[i]
        else:
            total += absolutes[i]

    return total


print(solution([4, 7, 12], [True, False, True]))
