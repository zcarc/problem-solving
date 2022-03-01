import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        pointer = self.table[index]
        while pointer:
            if pointer.key == key:
                pointer.value = value
                return
            if pointer.next is None:
                break
            pointer = pointer.next

        pointer.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size

        if self.table[index].value is None:
            return -1

        pointer = self.table[index]
        while pointer:
            if pointer.key == key:
                return pointer.value
            pointer = pointer.next

        return -1

    def remove(self, key: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            return

        if self.table[index].key == key:
            self.table[index] = ListNode() if self.table[index].next is None else self.table[index].next
            return

        pointer = self.table[index]
        prev = pointer
        while pointer:
            if pointer.key == key:
                prev.next = pointer.next
                return
            prev, pointer = pointer, pointer.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)