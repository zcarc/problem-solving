# 2022.02.19


# 내 풀이
def solution(n, lost, reserve):

    _lost = [l for l in lost if l not in reserve]
    _reserve = [l for l in reserve if l not in lost]

    _lost.sort()
    _reserve.sort()

    while _reserve:
        r = _reserve.pop()
        for i in range(len(_lost) - 1, -1, -1):
            if _lost[i] - 1 == r or _lost[i] + 1 == r:
                _lost.pop(i)
                break

    return n - len(_lost)


# 다른사람 풀이

# 풀이 1.
def solution(n, lost, reserve):
    _lost = [l for l in lost if l not in reserve]
    _reserve = [l for l in reserve if l not in lost]

    _lost.sort()
    _reserve.sort()

    for r in _reserve:
        if r - 1 in _lost:
            _lost.remove(r - 1)
        elif r + 1 in _lost:
            _lost.remove(r + 1)

    return n - len(_lost)


# 풀이 2.
def solution3(n, lost, reserve):

    answer = n - len(lost)

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                lost[i] = -1
                reserve[j] = -1
                answer += 1
                break

    lost.sort()
    reserve.sort()

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] - 1 == reserve[j] or lost[i] + 1 == reserve[j]:
                lost[i] = -1
                reserve[j] = -1
                answer += 1
                break

    return answer