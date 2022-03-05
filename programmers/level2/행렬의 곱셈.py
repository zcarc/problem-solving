def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            acc = 0
            for k in range(len(arr1[i])):
                acc += arr1[i][k] * arr2[k][j]
            tmp.append(acc)
        answer.append(tmp)

    return answer


arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))


# 곱셉을 할 때 k번째 위치는 arr1, arr2에서 같은 위치에서 계속 반복되므로 k로 지정했다.
# arr2의 행의 개수만큼 반복되므로 arr2[0]이 계속 반복된다.