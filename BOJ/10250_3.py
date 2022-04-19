a = int(input())

for _ in range(a):
    h, w, n = list(map(int, input().split()))
    print('{0}{1:0>2}'.format((n - 1) % h + 1, (n - 1) // h + 1))
