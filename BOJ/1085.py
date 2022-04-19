x, y, w, h = list(map(int, input().split()))

x = min(x, w - x)
y = min(y, h - y)

print(min(x, y))
