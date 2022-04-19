a = int(input())
cnt = 0

for _ in range(a):
    s = input()
    duplicated = 0
    for idx in range(len(s) - 1):
        if s[idx] == s[idx+1]:
            continue
        elif s[idx] != s[idx+1]:
            ns = s[idx+1:]
            if ns.count(s[idx]) > 0:
                duplicated += 1
    if duplicated == 0:
        cnt += 1

print(cnt)