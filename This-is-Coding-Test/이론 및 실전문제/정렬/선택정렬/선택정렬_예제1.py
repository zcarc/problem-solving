
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    minIndex = i
    for j in range(i + 1, len(array)):
        if array[minIndex] > array[j]:
            minIndex = j
    array[i], array[minIndex] = array[minIndex], array[i]

print(array)


# 가장 작은 데이터를 찾을 때 선택 정렬이 적합한 정렬 알고리즘이다.

# 시간 복잡도
# 평균: O(N^2)