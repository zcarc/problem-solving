# int형 배열과 target int를 각각 하나씩 받아서
# 해당 배열을 반복해서 target이 되면 두개의 index를 반환한다.
# 반환 형태는 list() 자료형에 append 하는식으로 추가하면 된다.

# 대충 풀이를 해보자면 이중 for문을 돌아서 하나씩 더해주는걸로 해본다.

# 내 풀이
nums = [2, 3, 4]
target = 6

nums2 = [2, 4, 3]
target2 = 6

nums3 = [3,3]
target3 = 6

nums4 = [4, 2, 3]
target4 = 6

nums5 = [1, 11, 15, 2, 17, 7, 19]
target5 = 9

# 내 풀이
def f():
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# 풀이 1. 브루트 포스로 계산
def twoSum():
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]



# 풀이 2. in을 활용한 문제풀이
def t(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            print(f'nums[i + 1:]: {nums[i + 1:]}')
            print(f'nums[i + 1:].index(complement): {nums[i + 1:].index(complement)}')
            print(f'nums[i + 1:].index(complement) + (i + 1): {nums[i + 1:].index(complement) + (i + 1)}')
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

        # print(f'complement: {complement} / target: {target} / n: {n} / i: {i}')
        # print(f'nums[i + 1:] == {nums[i + 1:]}')


# 풀이 2를 변형
def t_2(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            print(f'nums[i + 1:]: {nums[i + 1:]}')
            print(f'nums[i + 1:].index(complement): {nums[i + 1:].index(complement)}')
            print(f'nums[i + 1:].index(complement) + (i + 1): {nums[i + 1:].index(complement) + (i + 1)}')
            print(f'i: {i} / n: {n}')
            return [i, nums.index(complement)]

        # print(f'complement: {complement} / target: {target} / n: {n} / i: {i}')
        # print(f'nums[i + 1:] == {nums[i + 1:]}')


# 풀이 2
def t_3(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


# print(t(nums, target))
# print()
# print(t(nums2, target2))
# print()
# print(t(nums3, target3))
# print()
# print(t(nums4, target4))
#
# print()
# print(t_2(nums, target))
# print()
# print(t_2(nums2, target2))
# print()
# print(t_2(nums5, target5))
# print()
#
nums6 = [2, 1, 3]
target6 = 4
# print(t_3(nums6, target6))


# 첫 번째 수를 뺀 결과 키 조회
def t_4(nums, target):
    nums_map = {}

    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    print(f'nums_map: {nums_map}')

    # 타겟에서 첫 번째 수를 뺀 결과르 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [i, nums_map[target - num]]


nums7 = [3, 2, 4, 3]
target7 = 6
# print(t_4(nums7, target7))
#
# print(t_4(nums3, target3))


# 풀이 4. 조회 구조 개선
# 풀이 3과 거의 비슷한 코드지만 좀 더 간결하게 작성한 코드라고 볼 수 있다.
# for의 조건문 if 최소 한번이라도 nums_map에 어떤 값을 넣었을 경우
# 그 다음 순회에서 조건이 참일경우가 있을수도 있다.
def t_5(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


# 풀이 5. 투포인터 이용
# 이 함수는 배열이 정렬된 상태에서만 사용가능하다 만약 정렬되지 않은 상태라면 함수를 사용할 수가 없으므로
# 함수를 사용하기 전에 배열에 있는 값들을 오름차순으로 정렬해야한다.
def t_6(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1

    while not left == right:
        print(f't_6... while not left == right... left: {left} / right: {right}')
        # 합이 타겟보다 작으면 왼쪽포인터를 오른쪽으로 이동
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크다면 오른쪽포인터를 왼쪽으로 이동
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


# 투포인터를 사용하는 방법인데 여기서 nums5는 정렬되지 않았으므로 답이나오지 않는다.
# 그래서 while는 무조건 실행은 하겠으나 같은 경우가 나오지 않으므로 return 하는 경우는 없다.
# 그래서 정렬하는 경우는 또 다를수가 있다.
print(t_6(nums5, target5))

# 투 포인터를 사용하고 시간복잡도가 O(n)이다. 배열이 정렬된 경우이므로 답이 나올 수 있다고 기대할 수 있다.
# 하지만 정렬하는 로직을 추가했다고 하더라도 답을 찾을 수가 없다.
# 이 문제는 값을 찾는게 아니라 인덱스를 반환하는 문제라서 정렬되지 않은 배열을 받았을 때 정렬을 하게 되면 원래 배열의 인덱스를 찾을 수 가 없다.
# 값을 찾는 문제였다면 이 함수로 답을 찾을 수 있지만 인덱스를 찾는 문제라서 정렬된 배열이 무조건 주어지지 않는다면 풀이할 수 없는 함수이다.
nums8 = [2,7,11,15]
target8 = 9
print(t_6(nums8, target8))
