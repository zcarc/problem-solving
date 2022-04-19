originNum = int(input())
newNum = originNum
cnt = 0

while True:
    a = divmod(newNum, 10)
    plus = a[0] + a[1]
    # print(f'plus = {plus}')

    onesPlace = plus % 10
    # print(f'onesPlace = {onesPlace}')

    newNum = int(str(a[1]) + str(onesPlace))
    cnt += 1
    # print(f'newNum = {newNum}')
    if newNum == originNum:
        # print(f'if... newNum = {newNum}, originNum = {originNum}')
        break

# print(newNum)
print(cnt)