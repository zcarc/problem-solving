# 내 풀이
def s(nums):
    nums.sort()
    sum = 0

    # from_mid = nums[len(nums) // 2:]

    # print(nums)
    # print(from_mid)

    for n in zip(nums[::2], nums[1::2]):
        print(n)
        print(f'type(n): {type(n)}')
        print(f'min(n): {min(n)}')

        sum += min(n)

    return sum


nums = [1,4,3,2]
# print(s(nums))

nums2 = [6,2,6,5,1,2]
# print(s(nums2))

# 풀이 1. 오름차순 풀이
def s1(nums):
    sum = 0
    pair = []
    nums.sort(reverse=True)

    for num in nums:
        pair.append(num)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


# print('s1...')
print(s1(nums))
# print(s1(nums2))

# 풀이 2. 짝수 번째 값 계산
def s2(nums):
    sum = 0
    nums.sort()

    for i, v in enumerate(nums):
        if i % 2 == 0:
            print(f'i: {i} / v: {v}')
            sum += v

    return sum


# print('s2...')
# print(s2(nums))
# print(s2(nums2))


# 풀이 3. 파이썬 다운 방식
def s3(nums):
    print(f'sorted: {sorted(nums)}')
    print(f'sorted: {sorted(nums)[::2]}')
    return sum(sorted(nums)[::2])

