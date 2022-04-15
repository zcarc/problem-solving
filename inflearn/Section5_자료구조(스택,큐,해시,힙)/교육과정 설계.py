from collections import deque


def solution():

    required = input()
    n = int(input())
    arr = [input() for _ in range(n)]

    for idx, row in enumerate(arr):
        dq = deque(list(required))

        for char in row:
            if char in dq:
                if dq.popleft() == char:
                    continue
                else:
                    print(f'#{idx + 1} NO')
                    break
        else:
            if dq:
                print(f'#{idx + 1} NO')
            else:
                print(f'#{idx + 1} YES')





solution()

