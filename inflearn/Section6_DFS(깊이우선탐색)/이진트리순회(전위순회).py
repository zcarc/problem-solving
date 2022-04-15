def solution():

    def dfs(n):
        if n > 7:
            return
        else:
            print(n, end='')
            dfs(n * 2)
            dfs(n * 2 + 1)

    dfs(1)


solution()