def solution(numbers, target):

    cnt = 0

    def dfs(level, acc):
        if level == len(numbers):
            if acc == target:
                nonlocal cnt
                cnt += 1
        else:
            dfs(level + 1, acc + numbers[level])
            dfs(level + 1, acc - numbers[level])

    dfs(0, 0)

    return cnt


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))

# 참고
# https://velog.io/@euneun/프로그래머스-타겟넘버C-BFSDFS
