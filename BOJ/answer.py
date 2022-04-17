n = int(input())

arr = [[0] * n for _ in range(n)]


def star(x, y, size, blank):

    if blank:
        for i in range(x, x + size):
            for j in range(y, y + size):
                arr[i][j] = ' '
        return

    if size == 1:
        arr[x][y] = '*'
        return

    dividedSize = size // 3
    count = 0
    for i in range(x, x + size, dividedSize):
        for j in range(y, y + size, dividedSize):
            count += 1

            if count == 5:
                star(i, j, dividedSize, True)
            else:
                star(i, j, dividedSize, False)

star(0, 0, n, False)
sb = []


for i in range(0, n):
    for j in range(0, n):
        sb.append(arr[i][j])
    sb.append('\n')

for c in sb:
    print(c, end='')
