import heapq

from util_custom import ListNode, chaining_nodes

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
# lists = [[]]

root = result = ListNode(None)
heap = []

for i in range(len(lists)):
    if lists[i]:
        print((lists[i].val, i, lists[i]))
        heapq.heappush(heap, (lists[i].val, i, lists[i]))

print(f'init heap: {heap}')
print()

for _ in range(8):
    print(f'loop... result: {chaining_nodes(result)}')

    node = heapq.heappop(heap)
    idx = node[1]
    result.next = node[2]

    print(f'after pop heap: {heap}')
    print(f'node: {node}')
    print(f'idx: {idx}')
    print(f'result.next: {chaining_nodes(result.next)}')

    result = result.next

    print(f'result: {chaining_nodes(result)}')

    if result.next:
        heapq.heappush(heap, (result.next.val, idx, result.next))

    print(f'after push heap: {heap}')
    print(f'root: {chaining_nodes(root)}')
    print()


print(f'root.next: {root.next}')