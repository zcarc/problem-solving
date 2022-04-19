a = int(input())

l = [input() for _ in range(a)]
list_cnt = [0] * len(l)
cnt = 1
for idx_i, i in enumerate(l):
    for j in i:
        if j == 'X':
            cnt = 0
        list_cnt[idx_i] += cnt
        cnt += 1
    cnt = 1

for i in list_cnt:
    print(i)