import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # 삽입
    def put(self, key: int, value: int) -> None:
        print('put...')
        index = key % self.size
        print(f'key: {key}, index: {index}')
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        print('인덱스에 노드가 존재하는 경우 연결 리스트 처리')
        p = self.table[index]
        while p:
            print(f'p.key: {p.key}, key: {key}')
            if p.key == key:
                print('p.key == key')
                p.value = value
                return
            if p.next is None:
                print('p.next is None')
                break
            print(f'before p = p.next')
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        print('remove...')
        index = key % self.size
        if self.table[index].value is None:
            print('인덱스에 아무런 노드가 없다면 리턴')
            return

        # 인덱스의 첫 번째 노드일때 삭제 처리
        p = self.table[index]
        if p.key == key:
            print('인덱스의 첫 번째 노드일때 삭제 처리')
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            print('while p...')
            print(f'p.key: {p.key}, key: {key} @')
            if p.key == key:
                print('if p.key == key:...')
                print(f'p.key: {p.key}, key: {key} @@')
                prev.next = p.next
                return
            prev, p = p, p.next

        print('인덱스에 해당 키가 없으므로 리턴 없음')


h = MyHashMap()
h.put(1, 2)
h.put(1001, 3)
h.put(2001, 4)
h.put(3001, 5)
print(f'###### h.remove(2001): {h.remove(2001)}')
# print(f'###### h.remove(2001): {h.remove(2001)}')
