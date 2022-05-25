import collections
import heapq

nums = [2,2,3,1,1,1]
k = 2


def s(nums, k):
    counter = collections.Counter(nums)
    heap = []

    print(f'counter: {counter}')

    for key in counter:
        print(f'(-counter[key], key): {(-counter[key], key)}')
        heapq.heappush(heap, (-counter[key], key))
        print(f'after heappush heap: {heap}')

    print(heap)

# print(s(nums, k))


# h = []
# heapq.heappush(h, 1)
# heapq.heappush(h, 3)
# heapq.heappush(h, 2)
# print(h)
#
# heapq.heappush(h, 4)
# heapq.heappush(h, 2)
# print(h)
#
# heapq.heappush(h, 7)
# heapq.heappush(h, 1)
# print(h)


# h = []
# heapq.heappush(h, 5)
# heapq.heappush(h, 1)
# heapq.heappush(h, 3)
# heapq.heappush(h, 4)
# heapq.heappush(h, 2)
# print(h)
#
# heapq.heappop(h)
# print(h)

h = []
heapq.heappush(h, 50)
heapq.heappush(h, 25)
heapq.heappush(h, 40)
heapq.heappush(h, 15)
heapq.heappush(h, 30)
heapq.heappush(h, 7)
print(h)

heapq.heappop(h)
print(h)