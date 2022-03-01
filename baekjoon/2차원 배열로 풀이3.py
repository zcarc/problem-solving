n = 9

size = n // 3
cnt = 0

tmp = [[0] * (size * 2) for i in range(size)]

print(tmp)

x = 0
y = 0

for i in range(x, size * 2):
    for j in range(y, size):
        i = i % 3
        print(f'for and for / i, j: {i, j}')






# tmpBreak = []
#
# for i in range(size):
#     for j in range(size * 2):
#         i = i % 3
#         tmpBreak.append(tmp[i][j])
#         if j > 0 and j % 5 == 0:
#             print(f'if j > 0 and j % 5 == 0 / j: {j}')
#             tmpBreak.append('\n')
#
# print(tmpBreak)
#
# for i in tmpBreak:
#     print(i, end='')

