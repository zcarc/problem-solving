import heapq


# 최소힙 오름차순 정렬
def heapsort(iterable):
    h = []
    result = []

    for e in iterable:
        heapq.heappush(h, e)

    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result


print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
