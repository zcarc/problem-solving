def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    # 중복을 허용한다면 if x <= pivot 으로 조건을 바꿔야한다.
    left_side = [x for x in tail if x < pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


array = [5,7,9,0,3,1,6,2,4,8]
print(quick_sort(array))


# 퀵정렬은 정렬되어 있지 않은 경우에 더 빠르게 동작하는 정렬 알고리즘이다.
# 데이터의 특성을 파악하기 어렵다면 퀵정렬을 이용하는 것이 유리하다.

# 시간복잡도
# 평균: O(NlogN)
# 최악: O(N^2)