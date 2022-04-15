
def solution():

    d1 = dict()
    d2 = dict()

    for c in input():
        d1[c] = d1.get(c, 0) + 1

    for c in input():
        d2[c] = d2.get(c, 0) + 1

    for k in d1.keys():
        if k in d2.keys():
            if d1[k] != d2[k]:
                return 'NO'
        else:
            return 'NO'

    else:
        return 'YES'


print(solution())





