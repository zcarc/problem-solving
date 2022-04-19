import sys
a = int(input())

for i in range(a):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)
