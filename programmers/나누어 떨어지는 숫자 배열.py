# 내 풀이.
def solution(arr, divisor):
    answer = []
    for e in sorted(arr):
        if e % divisor == 0:
            answer.append(e)

    if not answer:
        answer.append(-1)

    return answer