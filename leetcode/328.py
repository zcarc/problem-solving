from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e


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


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    # 예외 처리
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    # 반복하면서 홀짝 노드 처리
    while even and even.next:
        print(chaining_nodes(odd))
        print(chaining_nodes(even))
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
        print(chaining_nodes(odd))
        print(chaining_nodes(even))
        print()

    # 홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head
    return head


print(chaining_nodes(oddEvenList(a)))