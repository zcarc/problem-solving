n = int(input())

array = []
for _ in range(n):
    array.append(tuple(input().split()))

array = sorted(array, key=lambda x: x[1])

for e in array:
    print(e[0], end=' ')

