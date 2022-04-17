def solution():

    arr = list(map(int, input()))

    tmp = []
    cnt = 0

    def dfs(pointer):
        nonlocal cnt

        if pointer == len(arr):
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
                    if pointer < len(arr) - 1:
                        if arr[pointer] == int(str(i)[0]) and arr[pointer + 1] == int(str(i)[1]):
                            tmp.append(i)
                            dfs(pointer + 2)
                            tmp.pop()

    dfs(0)

    print(cnt)


solution()


# 정답
# 이 방법은 직접 풀었는데 3번 풀이와 달리 tmp를 스택으로 사용했다.