
# 풀이 (풀이참고)
def solution(h):

    answer = 0

    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    answer += 1

    return answer


print(solution(5))


# 처음 풀었던 풀이 (오답)
def solution2(h):

    answer = 0

    for i in range(h + 1):
        if i < 10 and i == 3:
            answer += 1
        elif i > 9:
            i = str(i)
            print(i)
            if i[0] == '3' or i[1] == '3':
                answer += 1

        for j in range(60):
            if j < 10 and j == 3:
                answer += 1
            elif j > 9:
                j = str(j)
                if j[0] == '3' or j[1] == '3':
                    answer += 1

            for k in range(60):
                if k < 10 and k == 3:
                    answer += 1
                elif k > 9:
                    k = str(k)
                    if k[0] == '3' or k[1] == '3':
                        answer += 1

    return answer


# print(solution2(5))