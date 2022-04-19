def solution(numbers):
    len_numbers = len(numbers)

    def permutation(max_len):
        arrival = [0] * max_len
        ch = [0] * len_numbers

        res = set()

        def dfs(level):
            if level == max_len:
                tmp = []
                for e in arrival:
                    tmp.append(e)
                res.add(tuple(tmp))
            else:
                for i in range(len_numbers):
                    if ch[i] == 1:
                        continue
                    ch[i] = 1
                    arrival[level] = numbers[i]
                    dfs(level + 1)
                    ch[i] = 0

        dfs(0)

        return res

    arr_p = []
    for i in range(1, len_numbers + 1):
        res = permutation(i)
        for e in res:
            arr_p.append(int(''.join(e)))

    set_p = set(arr_p)

    cnt = 0
    for e in set_p:
        if e < 2:
            continue
        elif e < 4:
            cnt += 1
        else:
            flag = True
            for i in range(2, int(e ** (1/2)) + 1):
                if e % i == 0:
                    flag = False
                    break

            if flag:
                cnt += 1

    return cnt


print(solution("17"))
print(solution("011"))