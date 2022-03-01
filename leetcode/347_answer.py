import collections
import heapq
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []
    # 힙에 음수로 삽입
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    print(freqs_heap)

    topk = list()
    # k번 만큼 추출, 민 힙 이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk


print(topKFrequent([4,4,4,2,2,2,2,2,3,3,5,5,5,5], 2))