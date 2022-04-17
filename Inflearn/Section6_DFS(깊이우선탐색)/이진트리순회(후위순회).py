def solution():

    def dfs(n):
        if n > 7:
            return
        else:
            dfs(n * 2)
            dfs(n * 2 + 1)
            print(n, end='')

    dfs(1)


solution()