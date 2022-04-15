
def solution():

    n = int(input())

    d = dict()

    for i in range(n):
        word = input()
        d[word] = 1

    for i in range(n - 1):
        word = input()
        d[word] = 0

    for k, v in d.items():
        if v == 1:
            return k


print(solution())