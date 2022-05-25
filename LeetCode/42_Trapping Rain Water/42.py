# 투 포인터를 최대로 이동
def trap(height):
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    # 여기서 이렇게 반복하는 이유는 어차피 반복하면서 left는 증가하고 right는 감소해서
    # 이 조건이 잘못될 경우는 없다.
    while left < right:
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

        if left_max < right_max:
            volume = volume + (left_max - height[left])
            left += 1
        else:
            volume = volume + (right_max - height[right])
            right -= 1

    return volume


height = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trap(height))


# 스택 쌓기
from typing import List

def trap_stack(height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            print(f'start while...')
            print(f'stack: {stack} / i: {i}')
            print(f'height[i]: {height[i]}')
            print(f'stack[-1]: {stack[-1]}')
            print(f'height[stack[-1]]: {height[stack[-1]]}')

            # 스택에서 꺼낸다
            top = stack.pop()
            print(f'top: {top}')

            if not len(stack):
                print(f'if not len(stack):...')
                print(f'end while...')
                print()
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            print(f'distance: {distance}')
            print(f'stack: {stack}')
            print(f'stack[-1]: {stack[-1]}')
            print(f'waters: {waters}')
            print(f'height[top]: {height[top]}')

            volume += distance * waters
            print(f'volume: {volume}')

            print(f'end while...')
            print()

        stack.append(i)
        print(f'after added i in stack: {stack} / i: {i}')
    return volume


# print(trap_stack([4,2,1,3]))
print(trap_stack([0,1,0,2,1,0,1,3]))


