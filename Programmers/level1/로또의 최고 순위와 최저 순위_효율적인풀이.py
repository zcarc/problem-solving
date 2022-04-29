def solution(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_0 = lottos.count(0)

    cnt = 0
    for e in win_nums:
        if e in lottos:
            cnt += 1

    return [rank[cnt_0 + cnt], rank[cnt]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
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
print(solution([10, 11, 12, 13, 14, 0], [20, 9, 3, 45, 4, 35]))
# print(solution([10, 11, 12, 13, 0, 0], [20, 9, 3, 45, 4, 35]))
# print(solution([10, 11, 12, 0, 0, 0], [20, 9, 3, 45, 4, 35]))

print(solution([10, 11, 12, 13, 14, 20], [20, 9, 3, 45, 4, 35]))
print(solution([10, 11, 12, 13, 9, 20], [20, 9, 3, 45, 4, 35]))