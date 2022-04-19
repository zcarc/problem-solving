a,b = map(int, input().split())

l = list(map(int, input().strip().split()))
for i in l:
    if b > i:
        print(i, end=' ')