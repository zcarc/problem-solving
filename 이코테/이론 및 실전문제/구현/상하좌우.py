def solution():

    n = int(input())
    directions = list(input().split())

    x = y = 1

    for direction in directions:
        if direction == 'U' and y > 1:
            y -= 1
        elif direction == 'D' and y < n:
            y += 1
        elif direction == 'L' and x > 1:
            x -= 1
        elif direction == 'R' and x < n:
            x += 1

    return f'{y} {x}'


# print(solution())


# 책 풀이 (기존풀이에서 소스코드 수정)
def solution2():

    n = int(input())
    directions = list(input().split())

    y, x = 1, 1

    # L, R, U, D
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    # 이동 계획(방향)을 하나씩 확인
    for direction in directions:
        ny, nx = 0, 0

        for i in range(len(move_types)):
            if direction == move_types[i]:
                ny = y + dy[i]
                nx = x + dx[i]
                # direction과 동일한 move_type을 찾았다면 더 이상 루프할 필요가 없어서 추가했다.
                break

        # 공간을 벗어나는 경우 무시
        if ny < 1 or ny > n or nx < 1 or nx > n:
            continue

        # 이동 수행
        y, x = ny, nx


    return (y, x)


print(solution2())