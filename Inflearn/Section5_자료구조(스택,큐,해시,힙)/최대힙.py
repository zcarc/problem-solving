import heapq


def solution():

    hq = []

    while True:
        n = int(input())

        if n == -1:
            break
        elif n == 0:
            if not hq:
                print(-1)
            else:
                print(-heapq.heappop(hq))
        else:
            heapq.heappush(hq, -n)


solution()