# 오름차순 기준으로 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)


# 삽입정렬은 정렬되어 있는 경우 더 빠르게 동작하는 정렬 알고리즘이다.

# 시간복잡도
# 평균: O(N^2)
# 최선: O(N)