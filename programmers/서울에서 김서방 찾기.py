# 2022.02.13

def solution(seoul):
    for i, v in enumerate(seoul):
        if v == "Kim":
            return f'김서방은 {i}에 있다'


seoul = ["Jane", "Kim"]
print(solution(seoul))


# 다른사람 풀이

# 풀이 1.
def s(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))


print(s(seoul))