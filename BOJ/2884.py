a,b = map(int, input().split())

if b - 45 < 0 and a == 0:
    print(23, 60 - abs(b - 45))

elif b - 45 < 0:
    print(a-1, 60 - abs(b - 45))

else:
    print(a, b-45)
