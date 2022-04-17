def solution():

    n = int(input())

    arr = [0] * 7
    result = []

    for _ in range(n):
        dice = list(map(int, input().split()))

        for die in dice:
            arr[die] += 1

        max_value = -2147000000
        for i in range(len(arr)):
            if arr[i] > max_value:
                max_value = arr[i]

        if max_value == 1:
            result.append(max(dice) * 100)
        elif max_value == 2:
            result.append(1000 + arr.index(max_value) * 100)
        elif max_value == 3:
            result.append(10000 + arr.index(max_value) * 1000)

        arr = [0] * 7

    return max(result)


print(solution())