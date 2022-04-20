import heapq as hq


def solution(scoville, K):
    total = 0
    cnt = 0

    while True:
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)
        total = a + (b * 2)
        cnt += 1

        if total >= K:
            return cnt
        elif not hq and total < K:
            return -1

        hq.heappush(scoville, total)


