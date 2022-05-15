def solution(w, h):
    targets = [1, 2, 1]

    cnt = 0
    for i in range(h):
        cnt += targets[i % 3]

    return w * h - cnt


print(solution(5, 5))