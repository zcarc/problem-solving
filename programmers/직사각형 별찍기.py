# 2022.02.09

# a, b = map(int, input().strip().split(' '))

# 내 풀이
def s(a, b):
    for x in range(b):
        print('*' * a)


# 다른사람 풀이

# 풀이 1.
def s2(a, b):
    answer = ('*' * a + '\n') * b
    print(answer)


# s2(5, 3)


# 풀이 2.
def s3(a, b):
    for i in range(b):
        for j in range(a):
            print('*', end='')
        print()


s3(5, 3)
