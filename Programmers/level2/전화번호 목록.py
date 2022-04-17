import collections


# 풀이 1. sort/loop로 풀이
def solution2(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True


# 풀이 2. 해시로 풀이
def solution3(phone_book):

    hash_map = collections.defaultdict(int)
    for phone in phone_book:
        hash_map[phone] = 1

    for phone in phone_book:
        tmp = ''
        for char in phone:
            tmp += char
            if tmp in hash_map and len(tmp) < len(phone):
                return False

    return True


print(solution3(["12", "123", "1235", "567", "88"]))


# 풀이 2번은 폰번호를 해시맵에 저장하고
# 번호를 문자별로 누적해서 더하기 위해서 반복해서 변수 tmp에 저장한다.
# tmp의 현재값이 해시맵에 있다면 해시맵에 있는 그 prefix가 현재 변수 phone의 prefix이므로 답이되어 False가 된다.
# 주의할점은 변수 tmp와 변수 phone이 같으면 안된다.
# tmp와 phone이 같은 상태에서 hash_map에 tmp가 있는지 확인하게 되면 hash_map의 prefix가 본인이 되어 False가 되어버린다.

# ["119", "97674223", "1195524421"] 일 때,
# for char in phone의 phone이 모두 반복을 돌아서 '' + '1' + '1' + '9' 가 되어 tmp = '119'가 된 상태고
# 여기서 if tmp in hash_map 는 true가 되는데 이 phone(=tmp)은 hash_map에 있는 key와 동일하므로 본인이라서 비교하지 않아야한다.
# 결국에는 tmp는 phone과 같으면 안되고 더 작아야하기 때문에 len(tmp) < len(phone)의 비교를 해주었다.(tmp != phone 도 가능하다.)