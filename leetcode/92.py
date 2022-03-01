from util_custom import ListNode, chaining_nodes

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


def reverseLinkedList(l: ListNode) -> ListNode:
    if l is None:
        return None

    prev = None
    while l:
        next, l.next = l.next, prev
        prev, l = l, next

    return prev


# print(chaining_nodes(reverseLinkedList(a)))


# def reverseLinkedList2(head):
#     if not head:
#         return head
#
#     root = start = ListNode(None)
#     root.next = head
#     print(chaining_nodes(root))
#
#     start = start.next
#     print(chaining_nodes(start))
#     end = start.next
#     print(chaining_nodes(end))
#
# print(chaining_nodes(reverseLinkedList2(a)))


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    # 예외 처리
    if not head or m == n:
        return head

    root = start = ListNode(None)
    root.next = head
    print(f'root: {chaining_nodes(root)}')
    print(f'start: {chaining_nodes(start)}')
    # start, end 지정
    for _ in range(m - 1):
        print('$')
        start = start.next
        print('$$')
    print(f'start: {chaining_nodes(start)}')
    end = start.next
    print(f'end: {chaining_nodes(end)}')
    print(f'after end first for root: {chaining_nodes(root)}')

    # 반복하면서 노드 차례대로 뒤집기
    for _ in range(n - m):
        print('@')
        tmp = start.next
        print(f'root: {chaining_nodes(root)}')
        start.next = end.next
        print(f'root: {chaining_nodes(root)}')
        end.next = end.next.next
        print(f'root: {chaining_nodes(root)}')
        print(f'tmp: {chaining_nodes(tmp)}')
        start.next.next = tmp
        print(f'root: {chaining_nodes(root)}')
        print('@@')
    return root.next


print(chaining_nodes(reverseBetween(a, 2, 5)))