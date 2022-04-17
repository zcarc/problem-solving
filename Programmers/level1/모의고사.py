import collections


# 내 풀이.
def solution(answers):

    result = []
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    hashMap = collections.defaultdict(int)

    for indexPattern, pattern in enumerate(patterns):
        for indexAnswer, answer in enumerate(answers):
            if answer == pattern[indexAnswer % len(pattern)]:
                hashMap[indexPattern + 1] += 1

    m = max(hashMap.values())
    for k, v in hashMap.items():
        if v == m:
            result.append(k)

    return result


answers = [1,2,3,4,5,6,7,8]
answers2 = [1,3,2,4,2]
# print(solution(answers))
print(solution(answers2))