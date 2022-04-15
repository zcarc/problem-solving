
def solution():

    n = int(input())

    arr = list(map(int, input().split()))

    left = 0
    right = n - 1

    last = 0
    tmp = []

    res = ''
    while left <= right:
        if arr[left] > last:
            tmp.append((arr[left], 'L'))

        if arr[right] > last:
            tmp.append((arr[right], 'R'))

        if len(tmp) == 0:
            break

        tmp.sort()

        res += tmp[0][1]

        if tmp[0][1] == 'L':
            left += 1
        else:
            right -= 1

        last = tmp[0][0]

        tmp.clear()

    return str(len(res)) + '\n' + res


print(solution())

