a = input()
sec = 0
dial = ['ABC',
        'DEF',
        'GHI',
        'JKL',
        'MNO',
        'PQRS',
        'TUV',
        'WXYZ']

for i in a:
    for j in dial:
        if i in j:
            sec += dial.index(j)+3
print(sec)