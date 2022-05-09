from collections import deque


def solution(bridge_length, weight, truck_weights):

    truck_weights = deque(truck_weights)
    bridge_on = deque()
    sum_bridge_on = 0
    time = 0

    while truck_weights:
        if len(bridge_on) < bridge_length:
            if sum_bridge_on + truck_weights[0] <= weight:
                waiting_truck = truck_weights.popleft()
                bridge_on.append(waiting_truck)
                sum_bridge_on += waiting_truck
            else:
                bridge_on.append(0)
            time += 1
        else:
            out_bridge = bridge_on.popleft()
            sum_bridge_on -= out_bridge

    return time + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(5, 5, [1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(solution(3, 1, [1, 1, 1]))


# 설명
# return time + bridge_length
# 마지막에 bridge_on에 append된 트럭이 해당 다리의 길이만큼 지나야하므로
# 현재 경과시간 + 다리길이 만큼해줘서 답을 구할 수 있다.

# 이 문제는 원래 테스트케이스 5번에서 시간초과가 발생한 문제였었는데 ("다리를 지나는 트럭_시간초과.py")
# sum(bridge_on) 를 사용하지 않고 다리에 올라간 합계를 구하는 변수 sum_bridge_on를 사용하니 시간초과가 되지 않고 풀 수 있었다.


# 참고
# https://mungto.tistory.com/4
