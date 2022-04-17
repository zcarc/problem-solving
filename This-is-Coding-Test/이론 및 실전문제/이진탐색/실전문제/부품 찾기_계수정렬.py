n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))

counting_array = [0] * 1000001

for e in array1:
    counting_array[e] = 1

for e in array2:
    if counting_array[e] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')