from collections import defaultdict


def solution(dirs):
    print('start')

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
                        print('if to_x == dx and to_y == dy:')
                        flag = True
                        break
                    elif d[(to_x, to_y)]:
                        for to_pos in d[(to_x, to_y)]:
                            to_dx, to_dy = to_pos
                            if cur_x == to_dx and cur_y == to_dy:
                                print('if cur_x == to_dx and cur_y == to_dy:')
                                flag = True
                                break

            d[(cur_x, cur_y)].append((to_x, to_y))
            cur_x = to_x
            cur_y = to_y

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