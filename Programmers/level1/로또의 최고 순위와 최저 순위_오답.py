def solution(lottos, win_nums):
    length = len(lottos)

    lottos.sort(reverse=True)
    win_nums.sort(reverse=True)
    ch = [0] * length

    cnt = 6
    zero_cnt = 0
    for i in range(length):
        is_same = False
        for j in range(length):
            # 체크하지 않은 당첨번호일 경우
            print(f'i: {i}, j: {j} lottos[i]: {lottos[i]}, win_nums[j]: {win_nums[j]}, ch[j]: {ch[j]}')
            if ch[j] == 0:
                # 로또번호와 당첨번호가 같거나, 로또번호가 0일 경우
                if lottos[i] == win_nums[j] or lottos[i] == 0:
                    ch[j] = 1
                    is_same = True
                    if lottos[i] == 0:
                        zero_cnt += 1
                    break

        # 로또번호가 당첨번호하고 일치하는 경우가 없는 경우
        if is_same is False:
            ch[i] = 1
            print(f'i: {i}, lottos[i]: {lottos[i]}')
            cnt -= 1

    print(lottos)
    print(win_nums)
    print(cnt, zero_cnt)

    highest = 6 - cnt + 1
    lowest = 6 - cnt + 1 + zero_cnt

    if highest == 7:
        highest -= 1
    if lowest == 7:
        lowest -= 1

    return [highest, lowest]


# print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
# print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
# print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))

# print(solution([1, 2, 5, 6, 7, 9], [20, 9, 3, 45, 4, 35]))
# print(solution([1, 2, 5, 6, 0, 9], [20, 9, 3, 45, 4, 35]))
# print(solution([0, 0, 0, 0, 0, 9], [20, 9, 3, 45, 4, 35]))
#
# print(solution([45, 4, 35, 20, 3, 1], [20, 9, 3, 45, 4, 35]))
# print(solution([45, 4, 35, 20, 3, 0], [20, 9, 3, 45, 4, 35]))


# print(solution([0, 0, 0, 0, 0, 0], [20, 9, 3, 45, 4, 35]))
# print(solution([0, 0, 0, 0, 0, 9], [20, 9, 3, 45, 4, 35]))
# print(solution([0, 0, 0, 0, 3, 9], [20, 9, 3, 45, 4, 35]))
# print(solution([0, 0, 0, 35, 3, 9], [20, 9, 3, 45, 4, 35]))
# print(solution([0, 0, 45, 35, 3, 9], [20, 9, 3, 45, 4, 35]))
# print(solution([0, 20, 45, 35, 3, 9], [20, 9, 3, 45, 4, 35]))
# print(solution([4, 20, 45, 35, 3, 9], [20, 9, 3, 45, 4, 35]))

# print(solution([10, 11, 12, 13, 14, 15], [20, 9, 3, 45, 4, 35]))
# print(solution([10, 11, 12, 13, 14, 0], [20, 9, 3, 45, 4, 35]))
# print(solution([10, 11, 12, 13, 0, 0], [20, 9, 3, 45, 4, 35]))
# print(solution([10, 11, 12, 0, 0, 0], [20, 9, 3, 45, 4, 35]))

print(solution([10, 11, 12, 13, 14, 20], [20, 9, 3, 45, 4, 35]))
print(solution([10, 11, 12, 13, 9, 20], [20, 9, 3, 45, 4, 35]))