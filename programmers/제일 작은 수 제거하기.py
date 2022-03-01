# 2022.02.11

# 내 풀이
def solution(arr):
    if len(arr) < 2:
        return [-1]

    arr.remove(min(arr))

    return arr


print(solution([10]))