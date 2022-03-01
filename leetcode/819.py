import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

paragraph = paragraph.lower()
paragraph = re.sub('[^\w\s]', '', paragraph)

d = {}
print(f'type(d): {type(d)}')
for p in paragraph.split():
    if p in d:
        d[p] += 1
    else:
        d[p] = 1

if banned:
    if banned[0] in d:
        del d[banned[0]]

mk = max(d, key=d.get)



print(f'mk: {mk}')
print(f'after deleted d: {d}')

print(f'd: {d}')
print(f'd.values(): {d.values()}')
print(f'max value: {max(d.values())}')

# 방법 1.
# 이 방법은 key를 반환하는데 반환하는 기준은 value를 비교해서 가장 큰 값을 비교하라는 의미이다.
# 이 방법을 사용해서 딕셔너리에 있는 값들 중에 가장 큰 값의 키를 가져올 수 있다.
print(f'max(d, key=d.get): {max(d, key=d.get)}')

print(f'd.get("bob"): {d.get("bob")}')
print(f'max(d): {max(d)}')
print(f'min(d): {min(d)}')


# 방법 2.
# 리스트 컴프리헨션 방법을 사용해서 해당 딕셔너리에서 키와 값을 가져와서 value가 가장 큰 값을 가져와서 해당 리스트에 넣는다.
# 여기서 비교는 딕셔너리 d에서 가장 큰 값을 계속 비교해서 가장 큰 값이라면 k를 반환하고 그 반환된 값이 ml 리스트에 원소로 들어간다.
ml = [k for k, v in d.items() if max(d.values()) == v]
print(f'ml: {ml}')


# 함수 정의
# 내가 쓴 풀이
def a(paragraph, banned):
    paragraph = paragraph.lower()
    paragraph = re.sub('[^\w]', ' ', paragraph)
    print(f'paragraph: {paragraph}')

    d = {}
    print(f'type(d): {type(d)}')
    for p in paragraph.split():
        if p in d:
            d[p] += 1
        else:
            d[p] = 1

    if banned:
        for b in banned:
            if b in d:
                del d[b]

    return max(d, key=d.get)


import collections

# 책 풀이
# colledctions.defaultdic(int)를 사용한 방법
# 이 방법을 사용하면 딕셔너리에 값이 있는지 확인할 필요가 없다.
def aa(paragraph, banned):
    words = [word for word in re.sub('[^\w]', ' ', paragraph)
             .lower().split()
             if word not in banned]

    # counts = collections.defaultdict(int)
    # for word in words:
    #     counts[word] += 1
    counts = collections.Counter(words)
    print(f'counts: {counts}')
    return counts.most_common(1)[0][0]

    print(f'type(counts): {type(counts)}')
    print(f'counts.most_common(1): {counts.most_common(1)}')
    print(f'counts.most_common(1)[0][0]: {counts.most_common(1)[0][0]}')
    print(f'counts.most_common(1)[0][1]: {counts.most_common(1)[0][1]}')
    print(f'counts.most_common(1): {counts.most_common(1)}')
    print(f'type(counts.most_common(1)[0]): {type(counts.most_common(1)[0])}')

    # return max(counts, key=counts.get)

    print(f'aa... words: {words}')
    print(f'a... counts: {counts}')

    print(f'max(counts, key=counts.get): {max(counts, key=counts.get)}')



aa(paragraph, banned)

case2 = "a, a, a, a, b,b,b,c, c"
banned_case2 = ["a"]

# b = a(case2, banned_case2)
b = a(paragraph, banned)

print(f'b: {b}')