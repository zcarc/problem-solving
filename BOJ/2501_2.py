import sys
input = sys.stdin.readline
n, k = map(int, input().split())

def findDivisors(n):
    l = []
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            l.append(i)
            l.append(n // i)

    l = list(set(l))
    l.sort()

    return l


l = findDivisors(n)

if len(l) >= k:
    print(l[k - 1])
else:
    print(0)
