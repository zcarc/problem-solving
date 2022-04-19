alpha = input()
a = ['c=',
     'c-',
     'dz=',
     'd-',
     'lj',
     'nj',
     's=',
     'z=']

for i in a:
    alpha = alpha.replace(i, '*')

print(len(alpha))