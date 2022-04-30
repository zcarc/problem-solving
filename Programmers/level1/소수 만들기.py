def solution(nums):
    length = len(nums)

    def is_prime(n):
        for i in range(2, int(n ** (1/2)) + 1):
            if n % i == 0:
                return False
        return True

    target_num = 3

    arrival = [0] * target_num

    answer = 0

    def dfs(level, start):
        if level == target_num:
            total = 0
            for e in arrival:
                total += e
            if is_prime(total):
                nonlocal answer
                answer += 1
        else:
            for i in range(start, length):
                arrival[level] = nums[i]
                dfs(level + 1, i + 1)

    dfs(0, 0)

    return answer


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))