from collections import deque


def solution():

    required = input()
    n = int(input())
    # arr = [input() for _ in range(n)]

    for i in range(n):
        arr = input()

        dq = deque(list(required))

        for char in arr:
            if char in dq:
                if dq.popleft() != char:
                    print(f'#{i + 1} NO')
                    break
        else:
            if not dq:
                print(f'#{i + 1} YES')
            else:
                print(f'#{i + 1} NO')





solution()

