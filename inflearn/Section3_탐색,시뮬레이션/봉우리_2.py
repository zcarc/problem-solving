def solution():

    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    arr.insert(0, [0] * n)
    arr.append([0] * n)

    for i in range(len(arr)):
        arr[i].insert(0, 0)
        arr[i].append(0)

    # 북남동서
    y = [-1, 1, 0, 0]
    x = [0, 0, 1, -1]

    peaks_cnt = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 모든 반복문의 조건이 참일 경우 True
            if all(arr[i][j] > arr[i + y[k]][j + x[k]] for k in range(4)):
                peaks_cnt += 1

    return peaks_cnt


print(solution())


