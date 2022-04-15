def solution():

    arr = list(map(int, input()))

    n = len(arr)

    arr.append(-1)

    tmp = [0] * n
    cnt = 0

    def dfs(level, pointer):
        nonlocal cnt

        if level == n:
            # tmp[pointer]에 i를 넣기 때문에 i가 2자리일 경우
            # 할당되는 값이 더 작아져서 tmp 전체가 아니라 pointer 길이만큼 순회해야한다.
            for i in range(pointer):
                print(chr(tmp[i] + 64), end='')
            print()
            cnt += 1
        else:
            for i in range(1, 27):
                if arr[level] == i:
                    tmp[pointer] = i
                    dfs(level + 1, pointer + 1)
                elif i >= 10:
                    if arr[level] == i // 10 and arr[level + 1] == i % 10:
                        tmp[pointer] = i
                        dfs(level + 2, pointer + 1)

    dfs(0, 0)

    print(cnt)


solution()


# 답안 참고해서 풀이
# 알파코드.py로 푼 방법은 level을 사용하지 않았고 tmp를 스택으로 활용하여 풀었는데,
# 알파코드.py의 pointer가 여기서는 level로 사용되고,
# 두번째 인자 pointer는 tmp의 index의 pointer로 사용된다.
