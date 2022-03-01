# 2022.02.09

# 내 풀이
def solution(phone_number):
    phone_number = list(phone_number)
    for i in range(len(phone_number) - 4):
        phone_number[i] = '*'

    return ''.join(phone_number)


# 다른사람 풀이

# 풀이 1.
def s(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[:-4]


print(s('027778888'))
