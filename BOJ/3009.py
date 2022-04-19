vertex1 = list(map(int, input().split()))
vertex2 = list(map(int, input().split()))
vertex3 = list(map(int, input().split()))

vertex4 = [0, 0]


if vertex1[0] == vertex2[0]:
    vertex4[0] = vertex3[0]

elif vertex1[0] == vertex3[0]:
    vertex4[0] = vertex2[0]

else:
    vertex4[0] = vertex1[0]


if vertex1[1] == vertex2[1]:
    vertex4[1] = vertex3[1]

elif vertex1[1] == vertex3[1]:
    vertex4[1] = vertex2[1]

else:
    vertex4[1] = vertex1[1]


print(vertex4[0], vertex4[1])
