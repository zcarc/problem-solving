def solution():

    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    left = 0
    right = 1

    total = arr[0]

    cnt = 0
    while True:
        if total < m:
            if right >= len(arr):
                break
            total += arr[right]
            right += 1
        elif total > m:
            total -= arr[left]
            left += 1
        else:
            cnt += 1
            total -= arr[left]
            left += 1

    return cnt


print(solution())


# <설명>
# if right >= len(arr):
#      break
# total이 작을 경우 right를 더해줘야하는데
# 만약 right가 arr를 범위를 벗어난 경우라면 더할 수 있는 값이 없으므로 break를 해줘야한다.
