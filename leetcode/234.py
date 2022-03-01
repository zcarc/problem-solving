import collections
from typing import Optional, List, Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 리스트 변환
def s(head: Optional[ListNode]) -> bool:
    q: List = []

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(1)

a.next = b
b.next = c
c.next = d

# print(s(a))


# 데크를 이용한 최적화
def s2(head: Optional[ListNode]) -> bool:
    q: Deque = collections.deque()

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


# print(s2(a))


# 런너를 이용한 우아한 풀이
def s3(head: Optional[ListNode]) -> bool:
    rev = None
    fast = slow = head

    # while fast.next: # 홀수인 경우 필요
    # while fast: # 짝수인 경우 필요
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        rev, slow = rev.next, slow.next

    return not rev


aa = ListNode(1)
bb = ListNode(2)
cc = ListNode(3)
dd = ListNode(5)
ee = ListNode(1)

aa.next = bb
bb.next = cc
cc.next = dd
dd.next = ee

# print(s3(aa))
# print(s3(a))

q = ListNode(3)
w = ListNode(5)
e = ListNode(3)

q.next = w
w.next = e

# print(s3(q))


