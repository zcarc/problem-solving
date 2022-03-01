# 2022.02.11

# 내 풀이
def solution(n: int):
    n = list(str(n))
    n.sort(reverse=True)

    return int(''.join(n))


print(solution(118372))
