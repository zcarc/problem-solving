apartment = [[0] * 15 for _ in range(15)]

for i in range(len(apartment)):
    apartment[i][0] = 1
    apartment[0][i] = i + 1

for i in range(1, len(apartment)):
    for j in range(1, len(apartment)):
        apartment[i][j] = apartment[i][j - 1] + apartment[i - 1][j]

a = int(input())
for i in range(a):
    tmp = []
    for j in range(2):
        tmp.append(int(input()))
    print(apartment[tmp[0]][tmp[1] - 1])
