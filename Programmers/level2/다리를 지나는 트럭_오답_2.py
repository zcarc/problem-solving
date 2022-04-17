from collections import deque


def solution(bridge_length, weight, truck_weights):

    truck_weights = deque(truck_weights)
    bridge_on = deque()
    time = 0

    for _ in range(len(truck_weights)):
        if len(bridge_on) < bridge_length:
            if sum(bridge_on) + truck_weights[0] <= weight:
                bridge_on.append(truck_weights.popleft())
                time += 1
            else:
                time += (bridge_length - 1)
                bridge_on.clear()
        else:
            bridge_on.popleft()

        print(time, bridge_on, truck_weights)

    if len(bridge_on) == bridge_length:
        if (sum(bridge_on) - bridge_on[0]) + truck_weights[0] <= weight:
            return time + len(truck_weights) + bridge_length
        else:
            return time + 1 + len(truck_weights) + bridge_length

    return time + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(5, 5, [1, 1, 1, 1, 1, 1, 1, 1, 1]))
# print(solution(3, 1, [1,1,1]))
