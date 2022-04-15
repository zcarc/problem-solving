def solution():

    def dfs(n):
        if n > 7:
            return
        else:
            dfs(n * 2)
            print(n, end='')
            dfs(n * 2 + 1)

    dfs(1)


solution()