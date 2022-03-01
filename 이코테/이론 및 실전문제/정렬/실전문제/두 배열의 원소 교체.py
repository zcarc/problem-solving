n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

print(a, b, sep='\n')


for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(a, b, sep='\n')
print(sum(a))