def solution(numbers):

    n = len(numbers)

    ch = [0] * n
    arr = [0] * n
    permutations = []

    def dfs(level):
        if level == n:
            permutations.append(''.join(map(str, arr)))
        else:
            for i in range(n):
                if ch[i] == 1:
                    continue
                ch[i] = 1
                arr[level] = numbers[i]
                dfs(level + 1)
                ch[i] = 0

    dfs(0)

    permutations.sort(reverse=True)

    return permutations[0]


print(solution([3, 30, 34, 5, 9]))


# 테스트케이스 실패
# 런타임 에러 1 ~ 6
# 시간 초과 7 ~ 11