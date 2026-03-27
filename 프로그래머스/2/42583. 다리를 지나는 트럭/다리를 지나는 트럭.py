from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    truck = deque(truck_weights)
    cnt = 0
    current_weight = 0
    while bridge:
        cnt += 1
        out_truck = bridge.popleft()
        current_weight -= out_truck
        if truck:
            if current_weight + truck[0] <= weight:
                in_truck = truck.popleft()
                bridge.append(in_truck)      
                current_weight += in_truck   
            else:
                bridge.append(0)
    return cnt