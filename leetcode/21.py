class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def s(l1, l2):
    print()
    print(f's... l1 = {chaining_nodes(l1)}, l2 = {chaining_nodes(l2)}')

    if not l1:
        print(f'if (not l1({chaining_nodes(l1)}))({not l1}):')
        print(f'l1({chaining_nodes(l2)}), l2({chaining_nodes(l1)}) = l2({chaining_nodes(l2)}), l1({chaining_nodes(l1)})')
        l1, l2 = l2, l1
        print()

    elif l2 and l1.val > l2.val:
        print(f'elif l2({chaining_nodes(l2)}) and l1.val({l1.val}) > l2.val({l2.val}):')
        print(f'l1({chaining_nodes(l2)}), l2({chaining_nodes(l1)}) = l2({chaining_nodes(l2)}), l1({chaining_nodes(l1)})')
        l1, l2 = l2, l1
        print()

    if l1:
        print(f'if l1({chaining_nodes(l1)}):')
        print(f's(l1.next({chaining_nodes(l1.next)}), l2({chaining_nodes(l2)}))')
        t1 = l1.next
        t2 = l2
        l1.next = s(l1.next, l2)
        print(f'l1.next({chaining_nodes(l1.next)}) = s(l1.next({chaining_nodes(t1)}), l2({chaining_nodes(t2)}))')

    print()
    print(f'before return l1 = {chaining_nodes(l1)}')
    return l1


a = ListNode(1)
b = ListNode(3)
c = ListNode(5)

d = ListNode(2)
e = ListNode(4)
f = ListNode(6)

a.next = b
b.next = c

d.next = e
e.next = f


# print(f'merged: {chaining_nodes(s(a, d))}')


a = ListNode(1)
b = ListNode(2)
c = ListNode(4)

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)

a.next = b
b.next = c

d.next = e
e.next = f

print(f'merged: {chaining_nodes(s(a, d))}')