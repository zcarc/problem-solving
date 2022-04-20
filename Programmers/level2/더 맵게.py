import heapq as hq


def solution(scoville, K):
    cnt = 0
    hq.heapify(scoville)

    while len(scoville) >= 2:
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)

        total = a + (b * 2)
        cnt += 1
        hq.heappush(scoville, total)

        if scoville[0] >= K:
            return cnt

    return -1


# heapfy()를 안써서 틀린 문제
# 원래 heapify()를 안쓰고 리스트에 바로 heapq.heappop(), heapq.heappush() 함수를 써도 된다고 생각했는데
# 그것은 heapq.heappush()를 하는 경우만 그렇다.
# 처음에 List가 Heap 아닌 상태에서 heapq.heappop() 함수를 쓰면 heap이 되지 않은 리스트의 첫번째 원소를 pop하는 것이었다.
# 그래서 처음에 heapq.heappop()을 하기 전에 List를 Heap으로 바꿔줘야한다.

# 잘못된 자료
# https://programmers.co.kr/questions/14948
# [0, 0], 0 일 때 답이 0 이라는 것을 참고하였으나 그것은 틀린 답이었다.

# 알게된 점
# 원래 힙은 루트노드가 최소라서 그 노드만 K 값 이상이면 다른 서브트리들은 그 이상인데 계속 풀리지가 않아서
# 결국에는 "더 맵게_오답_4.py" 에서 다른 서브트리의 노드들까지 검사하는 코드를 작성했는데 이렇게 할 필요가 없었다.
# 원래 개념을 알고 있었던 "Heap"이었지만 이 문제를 통해서 조금 더 알게되었다.

# 참고
# https://velog.io/@younge/프로그래머스-더-맵게-힙


print(solution([0,0,0,1], 0))
print(solution([0, 0], 0))
print(solution([0, 0], 1))
print(solution([1, 0], 1))
# print(solution([1, 2], 10))
# print(solution([2, 3], 0))
# print(solution([1, 1, 1], 4))
# print(solution([10, 10, 10, 10, 10], 100))
# print(solution([1, 2, 3, 9, 10, 12], 7))
# print(solution([0, 2, 3, 9, 10, 12], 7))
print(solution([0, 0, 3, 9, 10, 12], 7))
# print(solution([0, 0, 0, 0], 7))
# print(solution([0, 0, 3, 9, 10, 12], 7000))
# print(solution([0, 0, 3, 9, 10, 12], 0))
# print(solution([0, 0, 3, 9, 10, 12], 1))
# print(solution([3, 9, 10, 12], 1))