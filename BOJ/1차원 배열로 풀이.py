n = 9

arr = [0] * n
for i in range(n):
    if i == 4:
        arr[i] = ' '
        continue
    arr[i] = '*'


tmp = []
for i in range(0, n):
    tmp.append(arr[i])
    if i == 2 or i == 5:
        tmp.append('\n')


print(arr)

for i in tmp:
    print(i, end='')
