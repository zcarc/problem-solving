# 내가 쓴 답
# n(행), m(열)
def solution():

    n, m = map(int, input().split())

    answer = 0

    for i in range(n):
        row = list(map(int, input().split()))
        minimum = min(row)
        answer = max(minimum, answer)

    return answer


print(solution())


