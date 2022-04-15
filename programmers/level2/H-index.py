def solution(citations):
    citations.sort(reverse=True)
    citations = [-1] + citations
    n = len(citations)

    for i in range(1, n):
        if i > citations[i]:
            return i - 1

    # 같은 수가 여러번 반복될 경우
    # 반복되는 수와 인덱스가 일치한다면 None이 떠서 마지막 인덱스를 반환해야함
    return n - 1


# print(solution([3, 0, 6, 1, 5]))
# print(solution([10, 8, 5, 4, 3]))
# print(solution([25, 8, 5, 3, 3]))
# print(solution([0, 0, 0, 0]))
# print(solution([1, 1, 1, 1]))
print(solution([3, 3, 3, 3]))
print(solution([3, 3, 3]))



# 참고
# https://en.wikipedia.org/wiki/H-index