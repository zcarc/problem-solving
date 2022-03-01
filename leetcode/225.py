import collections


class MyQueue:

    def __init__(self):
        self.dq = collections.deque()

    def push(self, x: int) -> None:
        self.dq.append(x)
        for _ in range(len(self.dq) - 1):
            self.dq.append(self.dq.popleft())

    def pop(self) -> int:
        return self.dq.popleft()

    def peek(self) -> int:
        return self.dq[0]

    def empty(self) -> bool:
        return len(self.dq) == 0


dq = MyQueue()
dq.push(1)
dq.push(2)
print(dq.peek())
print(dq.pop())
print(dq.empty())
