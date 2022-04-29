def solution(lottos, win_nums):
    length = len(lottos)

    lottos.sort(reverse=True)
    win_nums.sort(reverse=True)

    cnt = 6
    zero_cnt = 0
    for i in range(length):
        is_same = False
        for j in range(length):
            if lottos[i] == win_nums[j] or lottos[i] == 0:
                is_same = True
                if lottos[i] == 0:
                    zero_cnt += 1
                break

        if is_same is False:
            cnt -= 1

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