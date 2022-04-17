n = int(input())

arr = [[0] * n for _ in range(n)]

print('initial arr:', arr, sep="\n", end="\n\n")


def star(x, y, size, blank):
    print(f'@@ start star / x, y, size, blank: {x, y, size, blank}')

    if blank:
        print('###')
        print('blank...')
        for i in range(x, x + size):
            for j in range(y, y + size):
                arr[i][j] = ' '
                print(f'i, j: {i, j}')
                print('###')
        print(f'end function star blank @@')
        return

    if size == 1:
        arr[x][y] = '*'
        print(f'end function star size == 1 @@')
        return

    dividedSize = size // 3
    count = 0
    for i in range(x, x + size, dividedSize):
        print(f'@@@ start for i, x + n, size: {i, x + size, dividedSize}')
        for j in range(y, y + size, dividedSize):
            count += 1
            print(f'@@@@ start for j / i, j, count, y + size, dividedSize: {i, j, count, y + size, dividedSize}')

            if count == 5:
                star(i, j, dividedSize, True)
            else:
                star(i, j, dividedSize, False)
            print(f'@@@@ end for j / i, j, count, y + size, dividedSize: {i, j, count, y + size, dividedSize}', end='\n\n')
        print(f'@@@ end for i / i, j, count, y + size, dividedSize ; {i, j, count, y + size, dividedSize}', end='\n\n')

    print(f'end function star / i, j, count, y + size, dividedSize: {i, j, count, y + size, dividedSize} @@')


star(0, 0, n, False)
sb = []


for i in range(0, n):
    for j in range(0, n):
        sb.append(arr[i][j])
    print(f'for sb i, j: {i, j}', end="\n\n")
    sb.append('\n')

for c in sb:
    print(c, end='')


print('arr: ', arr, sep="\n")
print('sb: ', sb, sep="\n")
