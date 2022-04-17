def quick_sort(array, start, end):

    # 엇갈리거나 원소가 1개인 경우 종료
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    # 데이터가 2개 이상이거나 엇갈리지 않았다면
    while left <= right:
        # 인덱스가 초과되어 엇갈려도 상관없다 right에서 스왑한다.
        if left <= end and array[pivot] >= array[left]:
            left += 1
        # right >= start 로 조건을 걸면 스왑할 때 무한반복에 빠지게 된다.
        # 기존의 풀이와 다르게 array[pivot] <= array[right] 가 아닌
        # array[pivot] < array[right] 로 조건을 걸어도 정상적으로 정렬이 된다.
        if right > start and array[pivot] < array[right]:
            right -= 1

        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

    return array


array = [5,7,9,0,3,1,6,2,4,8]
print(quick_sort(array, 0, len(array) - 1))


# 퀵정렬은 정렬되어 있지 않은 경우에 더 빠르게 동작하는 정렬 알고리즘이다.
# 데이터의 특성을 파악하기 어렵다면 퀵정렬을 이용하는 것이 유리하다.

# 시간복잡도
# 평균: O(NlogN)
# 최악: O(N^2)