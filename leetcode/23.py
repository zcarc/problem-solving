import heapq
from typing import List
from util_custom import ListNode, chaining_nodes


def mergeKLists(lists: List[ListNode]) -> ListNode:
    root = pointer = ListNode(None)
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        pointer.next = node[2]

        pointer = pointer.next

        if pointer.next:
            heapq.heappush(heap, (pointer.next.val, idx, pointer.next))

    return root.next


a = ListNode(7)
b = ListNode(4)
c = ListNode(5)

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)

g = ListNode(2)
h = ListNode(6)


a.next = b
b.next = c

d.next = e
e.next = f

g.next = h

lists = [a, d, g]

print(chaining_nodes(mergeKLists(lists)))
# print(mergeKLists([[]]))