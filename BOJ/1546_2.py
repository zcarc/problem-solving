a = int(input())
l = list(map(int,input().split()))

s = sum(l)
m = max(l)

print(s/m*100/a)