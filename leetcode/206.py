class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 풀이 1. 재귀 구조로 뒤집기
def s(head):
    def ss(node, prev=None):
        if not node:
            return prev

        next, node.next = node.next, prev
        return ss(next, node)

    return ss(head)
    

a = ListNode(5)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(1)

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


# print(chaining_nodes(s(a)))


# 풀이 2. 반복 구조로 뒤집기
def t(head):
    prev = None
    node = head
    while node:
        next, node.next = node.next, prev
        node, prev = next, node

    return prev


print(chaining_nodes(t(a)))

