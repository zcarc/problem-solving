from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(list: ListNode) -> ListNode:
    prev = None
    node = list

    while node:
        next, node.next = node.next, prev
        node, prev = next, node

    return prev


def toList(linkedList: ListNode) -> []:
    list = []
    while linkedList:
        list.append(linkedList.val)
        linkedList = linkedList.next

    return list


def toReversedLinkedList(totalSum: str) -> ListNode:
    prev: Optional[ListNode] = None
    for x in totalSum:
        node = ListNode(int(x))
        node.next, prev = prev, node

    return prev


def addTwoNumbers(list1: ListNode, list2: ListNode) -> ListNode:
    l1 = toList(reverseLinkedList(list1))
    l2 = toList(reverseLinkedList(list2))

    s = int(''.join(str(x) for x in l1)) + \
        int(''.join(str(x) for x in l2))

    return toReversedLinkedList(str(s))


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c


def chaining_nodes(nodes) -> str:
    if nodes is None:
        return 'None'

    p = ''
    p += str(nodes.val)
    nodes = nodes.next
    while nodes:
        p += f'->{str(nodes.val)}'
        nodes = nodes.next

    return p


# print(chaining_nodes(reverseLinkedList(a)))
# print(toList(a))
# print(chaining_nodes(toReversedLinkedList('123')))

a = ListNode(2)
b = ListNode(4)
c = ListNode(3)

d = ListNode(5)
e = ListNode(3)
f = ListNode(7)

a.next = b
b.next = c

d.next = e
e.next = f

# print(chaining_nodes(addTwoNumbers(a, d)))


# 풀이 2. 전가산기 구현
def addTwoNumbers2(l1: ListNode, l2: ListNode) -> ListNode:
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        # 두 입력값의 합 계산
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        # 몫(자리올림수)과 나머지(값) 계산
        carry, val = divmod(sum + carry, 10)
        print(f'head == root: {head == root}')
        print(f'head.next == root.next: {head.next == root.next}')
        head.next = ListNode(val)
        head = head.next
        print(f'head: {chaining_nodes(head)}')
        print(f'root: {chaining_nodes(root)}')
        print(f'head.next: {chaining_nodes(head.next)}')
        print(f'root.next: {chaining_nodes(root.next)}')
        print()

    return root.next


print(chaining_nodes(addTwoNumbers2(a, d)))



# Test
# def chaning_nodes_instance(nodes: ListNode):
#     if nodes is None:
#         return 'None'
#
#     p = ''
#     p += str(nodes)
#     nodes = nodes.next
#     while nodes:
#         p += f' -> {str(nodes)}'
#         nodes = nodes.next
#
#     return p
#
#
# a1 = b1 = ListNode(10)
#
# print(f'a1: {chaining_nodes(a1)}')
# print(f'b1: {chaining_nodes(b1)}')
# print(f'a1 instance: {chaning_nodes_instance(a1)}')
# print(f'b1 instance: {chaning_nodes_instance(b1)}')
# print(f'a1 == b1: {a1 == b1}')
# print()
#
#
# print(f'Before assigning to the b1.next: {b1.next}')
# b1.next = ListNode(20)
# b1 = b1.next
#
# print(f'a1: {chaining_nodes(a1)}')
# print(f'b1: {chaining_nodes(b1)}')
# print(f'a1 instance: {chaning_nodes_instance(a1)}')
# print(f'b1 instance: {chaning_nodes_instance(b1)}')
# print(f'a1 == b1: {a1 == b1}')
# print()
#
#
# print(f'Before assigning to the b1.next: {b1.next}')
# b1.next = ListNode(30)
# b1 = b1.next
#
# print(f'a1: {chaining_nodes(a1)}')
# print(f'b1: {chaining_nodes(b1)}')
# print(f'a1 instance: {chaning_nodes_instance(a1)}')
# print(f'b1 instance: {chaning_nodes_instance(b1)}')
# print(f'a1 == b1: {a1 == b1}')
# print()
