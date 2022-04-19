# 소수일 경우 False
# 소수가 아닐 경우 True

s = 123456 * 2 + 1
l = [False] * s
l[0] = l[1] = True

for i in range(2, int(s ** (1 / 2)) + 1):
    if l[i] == True:
        continue
    for j in range(i * i, len(l), i):
        if j % i == 0:
            l[j] = True

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n + 1, (n * 2) + 1):
        if l[i] == False:
            cnt += 1

    print(cnt)
