def solution():

    arr1 = [0] * 52
    arr2 = [0] * 52

    for c in input():
        if c.isupper():
            arr1[ord(c) - 65] += 1
        else:
            arr1[ord(c) - 71] += 1

    for c in input():
        if c.isupper():
            arr2[ord(c) - 65] += 1
        else:
            arr2[ord(c) - 71] += 1

    for i in range(52):
        if arr1[i] != arr2[i]:
            return 'NO'
    else:
        return 'YES'


print(solution())