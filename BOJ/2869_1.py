A, B, V = list(map(int, input().split()))

day = int((V - B) / (A - B))
if int((V - B) % (A - B)) != 0:
    day += 1

print(day)
