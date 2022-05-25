import collections
import heapq


nums = [2,2,3,1,1,1]
k = 2


# 풀이 1. 우선순위 큐(heapq)와 카운터(Counter)로 풀이
def sSolution1(numbers, k):
    counter = collections.Counter(numbers)
    heap = []

    for key in counter:
        heapq.heappush(heap, (-counter[key], key))

    answer = []
    for _ in range(k):
        answer.append(heapq.heappop(heap)[1])

    return answer


print(Solution1(nums, k))


# 풀이 2. 파이썬다운 방식(Counter().most_common())
def Solution2(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


print(Solution2(nums, k))