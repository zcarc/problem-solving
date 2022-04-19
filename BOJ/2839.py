n = int(input())

answer = 0

if n == 4 or n == 7:
    answer = -1
elif n % 5 == 0:
    answer = n // 5
elif n % 5 == 1 or n % 5 == 3:
    answer = (n // 5) + 1
elif n % 5 == 2 or n % 5 == 4:
    answer = (n // 5) + 2

print(answer)
