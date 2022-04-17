import collections

nums = [2,2,3,1,1,1]

counter = collections.Counter(nums)
print(counter)

most2 = collections.Counter(nums).most_common(2)
print(most2, type(most2), type(most2[0]))
print(*collections.Counter(nums).most_common(2))

c1 = collections.Counter(nums).most_common(2)
print(f'c1: {c1}')

z = list(zip(collections.Counter(nums).most_common(2)))
print(f'z: {z}')

l1 = [11,22,33,333]
l2 = [44,55,66]
print(list(zip(l1, l2)))

print(list(zip(l2)))

t1 = (11, 22)
t2 = (33, 44)
print(list(zip(t1, t2)))

print(list(zip(t1)))
print(list(zip([t1])))

fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(fruits)

for f in fruits:
    print(f, end=' ')

print()


# 언패킹
print(*fruits)

lt = [(1, 3), (2, 2)]
print(f'lt: {lt}')
print(*lt)


# 패킹
def f(*params):
    print(f'params: {params}')


f('a', 'b', 'c')


# 키/값 언패킹
date_info = {'year': '2020', 'month': '01', 'day': '7'}
print(f'date_info: {date_info}')

new_info = {**date_info}
print(f'new_info: {new_info}')
