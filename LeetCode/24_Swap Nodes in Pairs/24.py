class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d


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


# 풀이 1. 변수 변경
def s(l: ListNode) -> ListNode:

    node = l
    while node and node.next:
        node.val, node.next.val = node.next.val, node.val
        node = node.next.next

    return l


# print(chaining_nodes(s(a)))


# 풀이 2. 반복
def s2(head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head
    print(f'0 root: {chaining_nodes(root)}')
    print(f'0 prev: {chaining_nodes(prev)}')
    print()

    while head and head.next:
        # b가 a(head)를 가리키도록
        b = head.next
        head.next = b.next
        print(f'1-0 b: {chaining_nodes(b)}')
        b.next = head
        print(f'1 root: {chaining_nodes(root)}')
        print(f'1 prev: {chaining_nodes(prev)}')
        print(f'1-1 b: {chaining_nodes(b)}')


        # prev가 b를 가리키도록
        prev.next = b
        print(f'2 root: {chaining_nodes(root)}')
        print(f'2 prev: {chaining_nodes(prev)}')

        # 다음 번 비교를 위해 이동
        head = head.next
        prev = prev.next.next
        print(f'3-0 root: {chaining_nodes(root)}')
        print(f'3-0 prev: {chaining_nodes(prev)}')
        print(f'3-0 head: {chaining_nodes(head)}')
        # print(f'3 root: {chaining_nodes(root)}')
        # print(f'3 prev: {chaining_nodes(prev)}')
        # print(f'3 head: {chaining_nodes(head)}')
        print()

    return root.next


# print(chaining_nodes(s2(a)))


def s3(head):
    root = prev = ListNode(None)
    prev.next = head

    while head and head.next:
        # 두 노드( head(a), b ) 스왑
        b = head.next
        head.next = b.next
        b.next = head

        # prev 다음 b를 가리키도록 설정
        prev.next = b

        # 다음 두 노드 스왑을 위해 설정
        head = head.next
        prev = prev.next.next

    return root.next


print(chaining_nodes(s3(a)))