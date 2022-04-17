import collections

J = 'aA'
S = 'aAAbbbb'

# 내 풀이
cnt = 0
for x in S:
    if x in J:
       cnt += 1

# print(cnt)

# 풀이 1. 해시 테이블
def numJewelsInStones1(jewels, stones):
    hash_table = {}

    for stone in stones:
        if stone in hash_table:
            hash_table[stone] += 1
        else:
            hash_table[stone] = 1

    cnt = 0
    for jewel in jewels:
        if jewel in hash_table:
            cnt += hash_table[jewel]

    return cnt


# print(numJewelsInStones1(J, S))


# 풀이 2. defaultdict를 이용해서 비교 생략
def numJewelsInStones2(jewels, stones):
    hash_table = collections.defaultdict(int)

    for stone in stones:
        hash_table[stone] += 1

    cnt = 0
    for jewel in jewels:
        cnt += hash_table[jewel]

    return cnt


# print(numJewelsInStones2(J, S))


# 풀이 3. Counter 클래스를 이용한 구현
def numJewelsInStones3(jewels, stones):
    counter = collections.Counter(stones)

    cnt = 0
    for jewel in jewels:
        cnt += counter[jewel]

    return cnt


# print(numJewelsInStones3(J, S))

# Counter 클래스로 생성된 인스턴스는 없는 key를 조회할 때 0을 반환만해주고 key를 생성해서 인스턴스에 저장하지는 않는다.
# defaultdict 같은 경우는 key가 없는 경우 해당 dict에 key를 0으로 생성을 해준다는점에서 Counter와 다르다.


# 풀이 4. 파이썬다운 방식 (리스트 컴프리헨션)
def numJewelsInStones4(jewels, stones):
    return sum(stone in jewels for stone in stones)


print(numJewelsInStones4(J, S))

# 모든 풀이 방식은 실행속도가 동일하다.
# 약간의 차이는 컴파일러의 수행 속도에 따른 오차 범위로 볼 수 있으며,
# 사실상 모두 동일하다고 봐도 무방하다.






















