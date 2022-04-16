from collections import deque


def solution(bridge_length, weight, truck_weights):

    truck_weights = deque(truck_weights)
    bridge_on = deque()
    time = 0

    while truck_weights:
        if len(bridge_on) < bridge_length:
            if sum(bridge_on) + truck_weights[0] <= weight:
                bridge_on.append(truck_weights.popleft())
            else:
                bridge_on.append(0)
            time += 1
        else:
            bridge_on.popleft()

    # 마지막에 brodge_on에 append된 트럭이 해당 다리의 길이만큼 지나야하므로
    # 현재 경과시간 + 다리길이 만큼해줘서 답을 구할 수 있다.
    return time + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(5, 5, [1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(solution(3, 1, [1,1,1]))
