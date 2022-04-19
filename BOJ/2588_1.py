A = int(input())
B = int(input())

one = B % 10
ten = B % 100

calc1 = A * one
calc2 = A * int(ten / 10)
calc3 = A * int(B / 100)

print(calc1, calc2, calc3, A * B, sep="\n")