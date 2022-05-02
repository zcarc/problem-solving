def solution(n):

    cnt = 0
    for i in range(1, n + 1):
        total = 0
        for j in range(i, n + 1):
            total += j
            if total == n:
                cnt += 1
                break
            # 이 부분을 추가하는 이유는 만약에 total의 크기가 n의 크기보다 더 크다면 답을 초과했으므로 더 이상 순회할 필요가 없고
            # 이 부분을 고려하지 않으면 효율성 테스트에서 시간초과가 된다.
            elif total > n:
                break

    return cnt


print(solution(15))