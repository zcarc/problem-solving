import collections


# 내 풀이
def solution(participant, completion):
    tmp = collections.defaultdict(int)

    for i in participant:
        tmp[i] += 1

    for i in completion:
        tmp[i] -= 1

    for k, v in tmp.items():
        if v == 1:
            return k


# 다른사람 풀이

# 풀이 1.
def s(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]