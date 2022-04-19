a = int(input())

for i in range(a):
    b = list(map(int,input().split()))
    m = max(b[1:])
    s = sum(b[1:])
    l = b[0]
    # avg = s/m*100/l
    avg = s / l
    cnt = 0
    for j in b[1:]:
        if avg < j:
            cnt += 1

    answer = (cnt/l)*100
    print(f'{answer:.3f}%')