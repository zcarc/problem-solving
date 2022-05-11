def solution(routes):

    routes.sort(key=lambda x: -(x[0]))

    stack = []

    cnt = 0
    for i in range(len(routes)):
        if not stack:
            stack.append(routes[i])
        else:
            if -(stack[0][0]) >= -(routes[i][1]):
                cnt += 1
                stack.clear()
            else:
                continue

    return cnt


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
print(solution([[-2, -1], [-4, -3], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
