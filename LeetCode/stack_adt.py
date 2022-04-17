# 연결 리스트를 이용한 스택 ADT 구현 (파이썬 알고리즘 인터뷰 p.234)

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)


for i in range(5):
    print(f'i: {i}, item: {stack.pop()}')
