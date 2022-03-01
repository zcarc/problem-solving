def solution():

    # 행, 열
    n, m = 4, 4

    # 좌표 정표, 방향
    a, b, direction = 1, 1, 0

    # 맵의 정보
    # 0: 육지, 1: 강
    game_map = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
    ]

    # 방문한 기록
    # 처음에는 모두 0으로 초기화 방문했다면 1로 변경
    visited_map = [[0] * m for _ in range(n)]

    # 처음 좌표 위치는 무조건 육지이고, 방문 했으므로 1로 변경
    visited_map[a][b] = 1

    # 북, 동, 남, 서 (시계 방향)
    # 캐릭터를 회전할 때는 시계 반대 방향으로 회전해야한다.
    move_a = [-1, 0, 1, 0]
    move_b = [0, 1, 0, -1]

    # 밟지 않은 땅을 밟은 횟수
    visited_cnt = 1

    # 캐릭터가 회전한 횟수
    turn_cnt = 0

    while True:
        # 캐릭터를 왼쪽으로 회전
        direction -= 1

        # 왼쪽에서 회전하기 때문에 북쪽에서 회전하면 서쪽이 되어야한다.
        if direction == -1:
            direction = 3

        # 캐릭터 회전 횟수 증가
        turn_cnt += 1

        # 다음에 이동할 a, b의 위치를 저장
        next_move_a = a + move_a[direction]
        next_move_b = b + move_b[direction]

        # 게임 맵과 방문한 맵 모두 방문하지 않았다면 해당 방향으로 이동
        if game_map[next_move_a][next_move_b] != 1 and visited_map[next_move_a][next_move_b] != 1:
            a = next_move_a
            b = next_move_b
            visited_map[a][b] = 1
            visited_cnt += 1
            turn_cnt = 0

        # 캐릭터가 4번을 회전했다면 뒤로 이동한다. (해당 땅을 밟은 캐릭터의 처음 방향)
        # 모두 가본 칸이거나 강이라면 회전을 4번할 수 있다.
        if turn_cnt == 4:
            next_move_a = a - move_a[direction]
            next_move_b = b - move_b[direction]

            # 뒤로 가려는 칸이 강이 있을 경우 종료한다.
            if game_map[next_move_a][next_move_b] == 1:
                break

            # 땅을 밟았던 방향과 같은 방향으로 뒤로 이동
            a = next_move_a
            b = next_move_b
            turn_cnt = 0

    return visited_cnt


print(solution())