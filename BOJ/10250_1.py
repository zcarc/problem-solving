a = int(input())

for _ in range(a):
    h, w, n = list(map(int, input().split()))
    room = n % h
    floor = n // h + 1
    if room == 0:
        room = h
        floor -= 1
    print(f'{room * 100 + floor}')
