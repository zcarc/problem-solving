
arr = [
    (1, 2),
    (3, 5),
    (2, 5),
]


arr.sort(key=lambda x: (x[1], x[0]))

print(arr)