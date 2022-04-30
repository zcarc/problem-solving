import itertools


def solution(nums):

    nums = list(itertools.combinations(nums, 3))

    def is_prime(n):
        for i in range(2, int(n ** (1 / 2)) + 1):
            if n % i == 0:
                return False
        return True

    answer = 0
    for e in nums:
        if is_prime(sum(e)):
            answer += 1

    return answer


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))