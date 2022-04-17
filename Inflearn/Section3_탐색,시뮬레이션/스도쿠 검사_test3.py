
matrix = []

for i in range(1, 37, 6):
    matrix.append(list(range(i, i + 6)))

for arr in matrix:
    print(arr)

print()

# 스도쿠에서 그룹 단위로 묶어서 생성
result = []
for i in range(2):
    for j in range(2):
        tmp = []
        for k in range(3):
            for s in range(3):
                tmp.append(matrix[i * 3 + k][j * 3 + s])

        result.append(tmp)

for x in result:
    print(x)