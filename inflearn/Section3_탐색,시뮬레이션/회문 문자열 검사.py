
def solution():

    n = int(input())

    for i in range(n):

        s = input()

        s = s.lower()

        for j in range(len(s) // 2):
            if s[j] != s[-1-j]:
                print(f'#{i + 1} NO')
                break
        else:
            print(f'#{i + 1} YES')


solution()