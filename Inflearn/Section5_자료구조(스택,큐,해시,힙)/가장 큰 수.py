def solution():

    nums, m = input().split()

    stack = [int(nums[0])]

    m = int(m)

    for e in nums[1:]:
        while stack and stack[-1] < int(e) and m > 0:
            stack.pop()
            m -= 1

        stack.append(int(e))

    if m > 0:
        stack = stack[:-m]

    return ''.join(map(str, stack))


print(solution())






