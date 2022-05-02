def solution(n):
    res = []

    def hanoi(n, f, b, t):
        if n == 1:
            res.append([f, t])
        else:
            hanoi(n - 1, f, t, b)
            res.append([f, t])
            hanoi(n - 1, b, f, t)

    hanoi(n, 1, 2, 3)

    return res


print(solution(2))


# 문제해설
# 이동하려는 원반이 2개라면 가장 위에 있는 원반은 두번째(by) 기둥으로 이동해야한다.
# 그래서 첫번째 재귀는 hanoi(n - 1, f, t, b) 가 된다.
# 그 다음 그 재귀가 끝나면 첫번째 기둥에 원반이 남아있는 상태라서 그 원반을 세번째 기둥(to)로 이동해줘야해서 res.append[[f, t]]를 해준다.
# 그 다음에 두번째 기둥에 있는 원반을 세번째 기둥으로 이동해야하기 때문에
# 두번째 재귀호출은 hanoi(n - 1, b, f, t)가 된다.