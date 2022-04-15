def solution():

    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())

    arr.sort(reverse=True)

    smallest = 21470000

    def dfs(level, acc):
        nonlocal smallest

        if smallest <= level:
            return

        if acc > m:
            return

        if acc == m:
            if level < smallest:
                smallest = level
            return
        else:
            for i in range(n):
                dfs(level + 1, acc + arr[i])
            return

    dfs(0, 0)

    return smallest


print(solution())


# 이 문제는 문제설명을 듣고 sort() 하는 부분 빼고 직접짜서 맞추었다.