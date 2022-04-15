
matrix = [[10,20,30,40,50,60], [100,200,300,400,500,600], [1000, 2000, 3000, 4000, 5000, 6000]]

result = []
for i in range(2):
    tmp = []
    for j in range(3):
        for k in range(3):
            tmp.append(matrix[i - i + j][i * 3 + k])

    result.append(tmp)
    

for x in result:
    print(x)
