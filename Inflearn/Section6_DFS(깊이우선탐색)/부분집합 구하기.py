def solution():

    n = int(input())

    ch = [0] * (n + 1)

    def dfs(level):
        if level == n + 1:
            for i in range(1, n + 1):
                if ch[i] == 1:
                    print(i, end=' ')
            print()

        else:
            ch[level] = 1
            dfs(level + 1)

            ch[level] = 0
            dfs(level + 1)

    dfs(1)


solution()
