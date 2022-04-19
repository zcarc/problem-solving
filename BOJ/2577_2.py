a = int(input())
b = int(input())
c = int(input())

l = list(str(a * b * c))

for i in range(10):
    print(int(l.count(str(i))))
