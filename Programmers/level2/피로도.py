def solution(k, dungeons):
    len_dungeons = len(dungeons)

    arrival = [[]] * len_dungeons
    visited = [0] * len_dungeons

    max_cnt = -2147000000

    def dfs(level):
        if level == len_dungeons:
            tmp_k = k
            cnt = 0
            for e in arrival:
                if tmp_k >= e[0]:
                    tmp_k -= e[1]
                    cnt += 1
            nonlocal max_cnt
            max_cnt = max(max_cnt, cnt)
        else:
            for i in range(len_dungeons):
                if visited[i] == 0:
                    visited[i] = 1
                    arrival[level] = dungeons[i]
                    dfs(level + 1)
                    visited[i] = 0

    dfs(0)

    return max_cnt


print(solution(80, [[80, 20], [50, 40], [30, 10]]))


# 설명
# 첫번째 풀이는 틀릴거 알면서 단순히 정렬로 풀어봤다.

# 두번째 풀이는 데크를 사용해서 k가 현재 원소의 최소피로도 보다 크다면,
# cnt 1 증가, k에서 현재 원소의 최소피로도만큼 감소, prev에 현재 원소 저장, 현재 원소를 삭제
# k가 현재 원소의 최소피로도 보다 작다면,
# cnt 1 감소, k에 prev의 최소피로도만큼 증가, 데크에 prev를 추가
# 결과는 테스트케이스 4, 18, 19를 제외하고 시간초과로 풀리지 않았다.