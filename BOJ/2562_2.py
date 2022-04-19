l = list()
for i in range(9):
    l.append(int(input()))

max_num = max(l)

print(max_num, l.index(max_num)+1, sep='\n')

