import heapq as hq


def solution(scoville, K):
    total = 0
    cnt = 0

    print(f'scoville: {scoville}, K: {K}')

    while len(scoville) >= 2:
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)

        total = a + (b * 2)
        print(total, a, b)
        cnt += 1

        if total == 0 and K == 0:
            return 0
        elif total >= K:
            return cnt

        hq.heappush(scoville, total)
        print(scoville)

    return -1


print(solution([0,0,0,1], 0))
print(solution([0, 0], 0))
print(solution([0, 0], 1))
print(solution([1, 2], 10))
print(solution([2, 3], 0))
print(solution([1, 1, 1], 4))
print(solution([10, 10, 10, 10, 10], 100))
print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([0, 2, 3, 9, 10, 12], 7))
print(solution([0, 0, 3, 9, 10, 12], 7))
# print(solution([0, 0, 0, 0], 7))
# print(solution([0, 0, 3, 9, 10, 12], 7000))
print(solution([0, 0, 3, 9, 10, 12], 0))
# print(solution([0, 0, 3, 9, 10, 12], 1), 2)