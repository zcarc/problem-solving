def solution(nums):
    len_selecting = len(nums) // 2
    len_set = len(set(nums))

    if len_set > len_selecting:
        return len_selecting
    else:
        return len_set


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 1, 1, 2, 2, 2]))


# 문제해설
# 중복을 제거한 후에 포켓몬 종류가 담긴 배열의 길이(len_set)가 선택할 포켓몬의 종류의 길이(len_selecting)보다 길다면
# 이미 중복을 제거했으므로 같은 종류의 포켓몬은 선택될 수 없으므로 서로 다른 종류의 포켓몬들만 선택될 것이다.
# 만약 nums = [1, 2, 3, 4, 5, 6] 일 때, len_set == 6 가 되고 모든 포켓몬들이 서로 다른 종류이므로 최대로 선택 가능한 횟수는 6이 된다.
# 하지만 문제에서는 len(nums) // 2 길이인 3 만큼 선택하라고 했으니 len_set 의 최대 선택 횟수가 6이지만 3을 반환해야 한다.

# nums = [1, 1, 1, 2, 2, 2] 일 때, len_set == 2 가 되고 서로 다른 종류는 2마리이므로 최대로 선택 가능한 횟수는 2가 된다.
# 선택해야할 포켓몬의 수는 len(nums) // 2 의 결과는 3 마리를 선택해야하지만 서로 다른 종류의 포켓몬이 2마리 밖에 없으므로 최대로 선택 가능한 횟수는 2가 된다.
# 그래서 답은 2가 된다.
