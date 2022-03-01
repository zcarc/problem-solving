array = [6, 5, 7, 9]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right >= start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)


# 14번째 줄 while(right >= start and array[right] >= array[pivot]):
# 조건을 while(right > start and array[right] >= array[pivot]): 해야한다
# 그렇지 않으면 right 값이 pivot 보다 작아지는 경우가 생겨서 무한 반복에 생기게 된다.
# 5,6,7,9 로 정렬된 다음에 게속 5,7,6,9 -> 5,6,7,9를 반복한다.
# 이유는 5,6,7,9 일 때, pivot = 2, start = 2, end = 3, left = 3, right = 3 이라면
# right 가 start 보다 크고 right번째 값이 start보다 더 크니 right를 빼준다.
# 그럼 pivot = 2, start = 2, end = 3, left = 3, right = 2 가 되고
# 여기서 멈춰야 하는데 멈추지 않고 같은 조건을 실행하면 다음과 같이 right가 pivot보다 더 앞쪽에 위치하게 된다.
# pivot = 2, start = 2, end = 3, left = 3, right = 1
# 그럼 pivot은 원래 자기보다 뒤쪽에 있는 right와 스왑을 해야하는데 자기보다 앞에 있는 right와 스왑하게 되어 다음과 같이 된다.
# 5,7,6,9
# 그래서 다시 right + 1, end로 quick_sort를 재귀호출하고
# pivot = 2, start = 2, end = 3, left = 3, right = 3 이 되고
# while(right >= start and array[right] >= array[pivot]): 이 조건이 한번 실행되어
# pivot = 2, start = 2, end = 3, left = 3, right = 2
# 두번 실행되어
# pivot = 2, start = 2, end = 3, left = 3, right = 1
# 그 다음 if(left > right) 이 조건으로 pivot과 right가 스왑된다.
# 5,6,7,9
# 계속해서 이렇게 무한 반복된다.