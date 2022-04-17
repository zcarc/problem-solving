
def solution():

    n = int(input())

    arr = list(map(int, input().split()))

    last = 0

    left = 0
    right = n - 1

    result = ''

    while left < right:
        tmp = [(arr[left], 'L'), (arr[right], 'R')]
        tmp.sort()

        for n, d in tmp:
            if n > last:
                if d == 'L':
                    left += 1
                    result += 'L'
                else:
                    right -= 1
                    result += 'R'
                last = n
                break
        else:
            break

    if left == right:
        if arr[left] > last:
            result += 'L'

    return str(len(result)) + '\n' + result


print(solution())
