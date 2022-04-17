if __name__ == "__main__":
    n, m = map(int, input().split())
    dis = [[5000] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dis[i][i] = 0

    for i in range(m):
        a, b, c = map(int, input().split())
        dis[a][b] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                print(f'k, i, j = {k, i, j}, dis[i][j]: {dis[i][j]}, dis[i][k] + dis[k][j]: {dis[i][k] + dis[k][j]}, dis[i][k]: {dis[i][k]}, dis[k][j]: {dis[k][j]}')
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

            for x in range(1, n + 1):
                print(dis[i][x], end=' ')
            print()
            print()

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                print("%-4s" % dis[i][j], end=' ')
            print()
        print()

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dis[i][j] == 5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')

        print()
