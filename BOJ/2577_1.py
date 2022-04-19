l = []
for i in range(3):
    l.append(int(input()))

sum_multiply = l[0]
for i in l[1:]:
    sum_multiply *= i

# l_cnt = [0] * 10
l_cnt = [0 for _ in range(10)]
for i in list(map(int, str(sum_multiply))):
    l_cnt[i] += 1

for i in l_cnt:
    print(i)