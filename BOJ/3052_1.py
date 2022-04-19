l = [int(input()) for _ in range(10)]

set_remainders = set()
for i in l:
    set_remainders.add(i % 42)

print(len(set_remainders))