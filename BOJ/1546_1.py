a = int(input())
l = list(map(int,input().split()))

m = max(l)
avg = [(i/m)*100 for i in l]

print(sum(avg)/a)