def solution():

    n = int(input())

    for i in range(1, n + 1):
        s = input()

        s = s.lower()

        if s == s[::-1]:
            print(f'#{i} YES')
        else:
            print(f'#{i} NO')


solution()