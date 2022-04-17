n = 9

size = n // 3
cnt = 0

tmp = [[0] * size for i in range(size * 2)]


for i in range(size * 2):
    for j in range(size):
        cnt += 1
        if cnt == 5:
            tmp[i][j] = ' '
            continue
        tmp[i][j] = '*'
    if i == 2 or i == 5:
        cnt = 0


print(tmp)


tmpBreak = []

for i in range(size * 2):
    for j in range(size):
        tmpBreak.append(tmp[i][j])
    tmpBreak.append('\n')

print(tmpBreak)

for i in tmpBreak:
    print(i, end='')

