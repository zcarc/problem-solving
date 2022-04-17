def solution(number, k):

    arrival = ['0'] * (len(number) - k)

    combi = []

    def dfs(level, start):

        if level == (len(number) - k):
            tmp = []
            for e in arrival:
                tmp.append(e)
            combi.append(tmp)
        else:
            for i in range(start, len(number)):
                arrival[level] = number[i]
                dfs(level + 1, i + 1)

    dfs(0, 0)

    res = sorted(combi, reverse=True)[0]

    return ''.join(res)


print(solution("1231234", 3))

