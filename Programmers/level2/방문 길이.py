from collections import defaultdict


def solution(dirs):

    d = defaultdict(list)

    cur_x = 0
    cur_y = 0

    x = [0, 0, 1, -1]
    y = [1, -1, 0, 0]

    cnt = 0
    for e in dirs:
        to_x = cur_x
        to_y = cur_y
        if e == 'U':
            to_x += x[0]
            to_y += y[0]
        elif e == 'D':
            to_x += x[1]
            to_y += y[1]
        elif e == 'R':
            to_x += x[2]
            to_y += y[2]
        elif e == 'L':
            to_x += x[3]
            to_y += y[3]

        if -5 <= to_x <= 5 and -5 <= to_y <= 5:
            flag = False
            if d[(cur_x, cur_y)]:
                for pos in d[(cur_x, cur_y)]:
                    dx, dy = pos
                    if to_x == dx and to_y == dy:
                        flag = True
                        break
            if d[(to_x, to_y)]:
                for to_pos in d[(to_x, to_y)]:
                    to_dx, to_dy = to_pos
                    if cur_x == to_dx and cur_y == to_dy:
                        flag = True
                        break

            d[(cur_x, cur_y)].append((to_x, to_y))
            cur_x = to_x
            cur_y = to_y

            if flag is False:
                cnt += 1

    return cnt


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("LLLLRRRRRRRRRRLLLLUUUUUUUUULLLLLLL"))
print(solution("ULURRDLLUL"))
print(solution("LLLLLLL"))
print(solution("LLLLLLLDRU"))
print(solution("LLLLLLLDRUD"))
print(solution("URULDD"))


# 설명
# 딕셔너리를 사용해서 두 가지 경우의 수를 확인해서 풀었습니다.
# 현재 위치에서 다음 좌표를 방문했을 경우와, 방문할 위치에서 현재 위치를 이미 방문했는지 확인했습니다.
# 이 두 가지의 경우는 해당 경로를 이미 지나쳤기 때문에 처음 걸어본 경로가 아닙니다.