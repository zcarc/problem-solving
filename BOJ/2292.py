inputHoneycomb = int(input())

currentHoneycomb = 1
cnt = 1

while currentHoneycomb < inputHoneycomb:
    currentHoneycomb = currentHoneycomb + 6 * cnt
    cnt += 1

print(cnt)