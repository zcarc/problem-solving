def solution():

    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    # 북남동서
    y = [-1, 1, 0, 0]
    x = [0, 0, 1, -1]

    peaks_cnt = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                if -1 < i + y[k] < n and -1 < j + x[k] < n:
                    move = arr[i + y[k]][j + x[k]]
                    # 이동한 위치가 현재 위치보다 크거나 같다면 현재 위치는 봉우리가 아니다.
                    if move >= arr[i][j]:
                        break
            # 이동한 위치가 현재 위치보다 크거나 같은 경우가 없다면 현재 위치는 봉우리가 맞다.
            else:
                peaks_cnt += 1

    return peaks_cnt


print(solution())


