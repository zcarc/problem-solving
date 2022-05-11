def solution(routes):

    routes.sort()

    speed_trap_position = routes[0][1]

    cnt = 1
    for i in range(1, len(routes)):
        if speed_trap_position > routes[i][0]:
            continue
        elif speed_trap_position == routes[i][0]:
            continue
        elif speed_trap_position < routes[i][0]:
            cnt += 1
            speed_trap_position = routes[i][1]

    return cnt


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
print(solution([[-2, -1], [-4, -3], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
