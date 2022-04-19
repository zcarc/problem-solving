import sys

input = sys.stdin.readline
int(input())

l = list(map(int, input().split()))
setSortedL = sorted(list(set(l)))

d = {setSortedL[i]: i for i in range(len(setSortedL))}

for i in l:
    print(d[i], end=" ")
