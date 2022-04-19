import sys
input = sys.stdin.readline
n = int(input())

l = map(int, input().split())

print(list(l).count(n))
