def solution(n):
    sum_n = 0
    cnt = 0

    for i in range(1, n + 1):

        sum_n = 0

        for j in range(i, n + 1):

            sum_n += j

            if sum_n == n:
                cnt += 1
                break

            elif sum_n > n:
                break

    return cnt


print(solution(15))