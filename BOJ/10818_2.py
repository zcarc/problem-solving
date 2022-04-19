a = int(input())

l = list(map(int, input().split()))

min = l[0]
max = l[0]

for i in l:
    if min > i:
        min = i
    elif max < i:
        max = i

print(min, max)