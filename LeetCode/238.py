from typing import List

def s(nums: List[int]) -> List[int]:
    out = []
    p = 1

    for i in range(len(nums)):
        out.append(p)
        print(f'i: {i}')
        print(f'p: {p}')
        print(f'out: {out}')
        p = p * nums[i]
        print(f'nums[i]: {nums[i]}')
        print(f'p * nums[i] : {p}')
        print()

    print(f'out: {out}')
    print()

    for i in range(len(nums) - 1, 0 - 1, - 1):
        print(i)



s([2, 3, 4, 5])
# s([-1,1,0,-3,3])