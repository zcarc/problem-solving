n, m = map(int, input().split())

# 여기서는 n이 행이되고, m이 열이 된다.
arr = [[False] * m for _ in range(n)]
answer = 64


def find(x, y, m):
    print(f'find... x: {x} y: {y}')

    end_x = x + 8
    end_y = y + 8
    count = 0

    # 첫번째 칸 색
    TF = arr[x][y]

    for i in range(end_x):
        for j in range(end_y):
            print(f'for... i: {i} j: {j}')

            # 올바른 색이 아닐경우 count 1 증가
            if arr[i][j] != TF:
                count += 1

            if TF:
                TF = False
            else:
                TF = True
            # TF = not TF

        # TF = not TF
        if TF:
            TF = False
        else:
            TF = True

    count = min(count, 64 - count)

    print(f'count: {count}, 64 - count: {64 - count}')
    print(f'min(count, 64 - count): {count}')
    print(f'm: {m}')

    m = min(m, count)

    print(f'min(m, count): {m}')

    return m


# 배열 입력
for i in range(n):
    row = input()

    for j in range(m):
        if row[j] == 'W':
            print(f'if row[j] == "W"... row: {row}')
            arr[i][j] = True
        else:
            arr[i][j] = False


print(f'arr: {arr}')

n_row = n - 7
m_col = m - 7

print(f'n_row(n - 7): {n_row}')
print(f'm_col(n - 7): {m_col}')

for i in range(n_row):
    for j in range(m_col):
        answer = find(i, j, answer)

print(answer)
