# LeetCode 622를 풀면서 큐와 원형큐의 차이점을 알고 싶어서 작성하게 되었는데
# 큐의 문제점인 빈 공간을 재활용 할 수 없다는점에서 원형 큐를 사용한다고 해서
# 이 큐가 사이즈가 꽉차고 삭제를 해서 다시 추가를 할 수 있는 지 확인해보기 위해서 Queue 모듈을 사용해서 직접 확인해본다.

import queue

q = queue.Queue(3)

print(f'q.qsize(): {q.qsize()}')
print(f'q.full(): {q.full()}')

q.put(1)
q.put(2)
q.put(3)

print(f'q.full(): {q.full()}')
q.put(10)

# print(f'q.full(): {q.full()}')
# print(f'q.qsize(): {q.qsize()}')
# q.put(20)
#
# print(q.get())
# print(q.get())
# print(q.get())