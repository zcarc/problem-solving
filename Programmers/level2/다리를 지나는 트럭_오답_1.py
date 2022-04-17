from collections import deque


def solution(bridge_length, weight, truck_weights):
    cnt = 0

    truck_weights = deque(truck_weights)
    dq = deque()

    dq.append(truck_weights.popleft())
    cnt += 1

    while dq:
        for _ in range(2):
            if sum(dq) + truck_weights[0] <= weight and truck_weights:
                dq.append(truck_weights.popleft())
                cnt += 1
            else:
                cnt += 1

            if cnt % bridge_length == 0:
                dq.popleft()
                break

        if not dq and truck_weights:
            dq.append(truck_weights.popleft())
            cnt += 1

    return cnt


print(solution(2, 10, [7, 4, 5, 6]))
