def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    result = [a * b for a, b in zip(A, B)]

    return sum(result)


A = [1,4,2]
B = [5,4,4]
print(solution(A, B))


# "곱한 값이 최소가 되기 위해서는, 큰 숫자 일 수록 작은 숫자와 곱해야 상대적으로 더 작은값" 이 나오게 된다.

