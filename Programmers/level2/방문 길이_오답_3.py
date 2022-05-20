from collections import defaultdict


def solution(dirs):

    d = defaultdict(list)

    cur_x = 0
    cur_y = 0

    x = [0, 0, 1, -1]
    y = [1, -1, 0, 0]

    cnt = 0
    for e in dirs:
        if -5 <= cur_x <= 5 and -5 <= cur_y <= 5:
            tmp_x = cur_x
            tmp_y = cur_y
            if e == 'U':
                tmp_x += x[0]
                tmp_y += y[0]
            elif e == 'D':
                tmp_x += x[1]
                tmp_y += y[1]
            elif e == 'R':
                tmp_x += x[2]
                tmp_y += y[2]
            elif e == 'L':
                tmp_x += x[3]
                tmp_y += y[3]

            flag = False
            if d[(cur_x, cur_y)]:
                for pos in d[(cur_x, cur_y)]:
                    dx, dy = pos
                    if tmp_x == dx and tmp_y == dy:
                        flag = True
                        break

            d[(cur_x, cur_y)].append((tmp_x, tmp_y))
            cur_x = tmp_x
            cur_y = tmp_y

            if flag is False:
                cnt += 1

    return cnt


print(solution("ULURRDLLU"))
# print(solution("LULLLLLLU"))
# print(solution("LLLLRRRRRRRRRRLLLLUUUUUUUUULLLLLLL"))
print(solution("ULURRDLLUL"))
# print(solution("LLLLLLL"))
print(solution("LLLLLLLDRU"))
print(solution("LLLLLLLDRUD"))

print(solution("URULDD"))