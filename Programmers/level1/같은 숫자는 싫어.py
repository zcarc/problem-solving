
arr = [1,1,3,3,0,1,1]


# 풀이 1. 배열에서 다음 인덱스 값과 비교
def s(arr):

    arr.append(10)

    answer = []
    for i in range(len(arr) - 1):

        if arr[i] != arr[i + 1]:
            answer.append(arr[i])

    return answer


print(s(arr))


# 풀이 2. 스택에 쌓인 값과 비교
def s2(arr):

    answer = [arr[0]]

    for phone in arr:
        if phone != answer[-1]:
            answer.append(phone)

    return answer