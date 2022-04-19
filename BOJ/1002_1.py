def pointOfContact(x1, y1, r1, x2, y2, r2):

    d = (x2 - x1) ** 2 + (y2 - y1) ** 2

    # 중점이 같으면서 반지름도 같은 경우
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1

    # 두 원의 반지름 합보다 중점 간 거리가 더 길 때
    elif d > (r2 + r1) ** 2:
        return 0

    # 원 안에 원이 있으나 내접하지 않을 때
    elif d < (r2 - r1) ** 2:
        return 0

    # 내접할 때
    elif d == (r2 - r1) ** 2:
        return 1

    # 외접할 때
    elif d == (r2 + r1) ** 2:
        return 1

    # 교점이 2개일 때
    elif d > (r2 - r1) ** 2:
        return 2


t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    print(pointOfContact(x1, y1, r1, x2, y2, r2))
