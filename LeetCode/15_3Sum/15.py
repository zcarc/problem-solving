from typing import List


# 투 포인터를 사용해서 풀이
def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()
    print(f'after sort nums: {nums}')
    print()

    # range(len(nums) - 2) 여기서 -2의 의미는
    # i는 현재 인덱스, left로 i + 1을 해주고 right로 끝 index 끝을 조회한다.
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        # i가 0보다 크고 1이상일 때 그 전 값과 같다면 다음 i로 넘어간다.
        # 만약 이 부분이 없다면 입력 값이 [-4, -1, -1, 0, 1, 2] 일 때
        # [-1. 0, 1], [-1, 0, 1] 이렇게 중복되어서 들어간다.
        if i > 0 and nums[i] == nums[i - 1]:
            print(f'if i > 0 and nums[i] == nums[i - 1]:...')
            print(f'i: {i}, nums[i]: {nums[i]}, nums[i - 1]: {nums[i - 1]}')
            continue

        # 간격을 좁혀가며 합 `sum` 계산
        left, right = i + 1, len(nums) - 1
        print(f'before start while...')
        print(f'i: {i}, left: {left}, right: {right}')

        # right는 가장 처음에 left보다는 크게 설정되어 있으므로
        # left가 커지거나 right가 작아지면 서로 가까워진다.
        while left < right:

            # 현재 인덱스의 값 + 인덱스 + 1의 값 + 인덱스의 끝값 = 이렇게 더한 값이 0이 되도록 하는 로직을 뒤에서 만든다.
            sum = nums[i] + nums[left] + nums[right]
            print(f'nums: {nums}')
            print(f'i: {i}, left: {left}, right: {right}')
            print(f'nums[i], nums[left], nums[right]: {nums[i], nums[left], nums[right]}')
            # print(f'i, left, right: {i, left, right}')
            print(f'sum: {sum}')
            print()

            # 이 sum을 0을 기준으로 0보다 크다면 left를 증가시키고
            # 0보다 작다면 right를 감소시킨다.
            # 만약 sum 이 0이라면 각각의 값을 results에 리스트 형태로 append 해준다.
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # `sum = 0`인 경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left], nums[right]])
                print(f'after append results: {results}')


                # 아래의 while 두 값은 left와 right에 서로 인접한 중복된 값이 있는 지 확인하는 로직이다.
                # 만약 아래의 두 while이 없고 input: [-2, 0, 0, 2, 2] 이렇게 받았다면 중복된 값이 배열에 추가된다.
                # 가장 처음에 i: 0, left: 1, right: 4 / -2, 0, 2 인 경우에 else: 문이 실행되어 윗줄에서
                # results 배열에 이미 해당 값을 추가시킨다.
                # 그 다음에는 i: 0, left: 2, right: 3 인 경우에 results 배열에 해당 값이 추가된다.
                # 여기서 확인할 수 있듯이 인덱스 1의 0과 인덱스 4의 2가 else문에서 추가된다음에
                # left += 1, right -= 1 을 해줌으로써 다시 인덱스 2가 0가 되고 인덱스 3이 2가 되어서
                # 0, 1, 4 / 0, 2, 3 인 경우는 sum = 0 이 되고 값 또한 같은 값을 같게 된다.
                # 인덱스는 다르지만 값은 서로 같기 때문에 이 코드를 작성할 때는 중복을 해주고 위해서
                # 해당 left, right 번째에 있을 경우 추가를 해준다.

                # 여기서 left의 현재값과 left의 현재값 보다 + 1 값이 같다면
                # left += 1 을 해준다.
                # [-1, -1, -1, -1, 2]
                # else: 성립하고 while left < right and nums[left] == nums[left + 1] 하고 같은 경우를 인덱스로 나열해보자면
                # index: 0, 1, 4 / 0, 2, 4
                # 위와 같이 두가지의 경우가 있다.
                # left 1, left 2 의 인덱스가 각각 -1 이므로 -1, -1, 2는 0
                # left 2, left 3 의 인덱스가 각각 -1 이므로 -1, -1, 2는 0
                while left < right and nums[left] == nums[left + 1]:
                    print(f'while left < right and nums[left] == nums[left + 1]:...')
                    print(f'i: {i}, left: {left}, right: {right}')
                    print(f'nums[left]: {nums[left]}, nums[left + 1]: {nums[left + 1]}')
                    left += 1
                    print(f'after plus left: {left}')
                    print()
                #
                #
                # 여기서 right의 현재값과 right의 현재값 보다 - 1 값이 같다면
                # right -= 1 을 해준다.
                while left < right and nums[right] == nums[right - 1]:
                    print(f'while left < right and nums[right] == nums[right - 1]:...')
                    print(f'left: {left}, right: {right}')
                    print(f'nums[right]: {nums[right]}, nums[right + 1]: {nums[right - 1]}')
                    right -= 1
                    print(f'after minus right: {right}')
                    print()

                left += 1
                right -= 1
                print(f'before end else...')
                print(f'left: {left}')
                print(f'right: {right}')
                print()

    return results


# nums = [-1, 0, 1, 2, -1, -4]
# print(threeSum(nums))

print('###')

# nums2 = [-2,0,0,2,2]
# print(threeSum(nums2))

# num3 = [-2,0,0,2,2]
# print(threeSum(num3))

num4 = [2,-1,-1,-1,-1]
print(threeSum((num4)))
