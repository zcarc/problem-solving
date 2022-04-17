from collections import deque


def solution():

    required = input()

    n = int(input())

    subjects = [deque([(i, v) for i, v in enumerate(input())]) for _ in range(n)]

    for idx, row in enumerate(subjects):
        tmp = []

        for r in required:
            while True:
                popped = row.popleft()
                if r == popped[1]:
                    tmp.append(popped)
                    break
                else:
                    row.append(popped)

        tmp.sort()
        res = ''
        for x in tmp:
            res += x[1]

        if res == required:
            print(f'#{idx + 1} YES')
        else:
            print(f'#{idx + 1} NO')


solution()


