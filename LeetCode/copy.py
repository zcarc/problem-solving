import copy

a = [1, 2, [3, 5], 4]
b = a
a[2][0] = 6

print(a, b)
print(id(a), id(b))


# 2차원 배열을 deepcopy로 참조가 다른 새로운 배열을 만든다.
c = [1, 2, [3, 5], 4]
d = copy.deepcopy(c)
c[2][0] = 6
print(c, d)
print(id(c), id(d))


# 3차원 배열도 deepcopy가 된다.
e = [1, 2, [3, [8, 9], 5], 4]
f = copy.deepcopy(e)
e[2][1][0] = 33
print(e, f)
print(id(e), id(f))