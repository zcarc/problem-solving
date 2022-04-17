def solution():

    arr = list(map(int, input()))

    arr.append(-1)

    tmp = []
    cnt = 0

    def dfs(pointer):
        nonlocal cnt

        if pointer == len(arr) - 1:
            for x in tmp:
                print(chr(x + 64), end='')
            print()
            cnt += 1
        else:
            for i in range(1, 27):
                if i // 10 == 0:
                    if arr[pointer] == i:
                        tmp.append(i)
                        dfs(pointer + 1)
                        tmp.pop()
                else:
                    if arr[pointer] == int(str(i)[0]) and arr[pointer + 1] == int(str(i)[1]):
                        tmp.append(i)
                        dfs(pointer + 2)
                        tmp.pop()

    dfs(0)

    print(cnt)


solution()

