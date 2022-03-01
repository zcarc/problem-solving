import collections

p1 = ["marina", "josipa", "nikola", "vinko", "filipa", "marina", "marina", "marina"]
c1 = ["josipa", "filipa", "marina", "nikola"]

res = collections.Counter(p1) - collections.Counter(c1)

print(p1)
print(c1)
print(collections.Counter(p1))
print(collections.Counter(c1))
print(res)
print(res.keys())
print(res.values())
print(list(res.keys())[0])
print(list(res.values())[0])
