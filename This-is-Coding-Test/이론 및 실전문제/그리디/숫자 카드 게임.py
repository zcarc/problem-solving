# 내가 쓴 답
# n(행), m(열)
def solution():

    n, m = map(int, input().split())

    matrix = []

    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    minimum_arr = []
    for row in matrix:
        minimum_arr.append(min(row))

    return max(minimum_arr)


print(solution())


