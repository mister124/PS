from collections import deque
def solution(arr):
    dq = deque()
    for num in arr:
        if len(dq) != 0 :
            if dq[-1] != num:
                dq.append(num)
        else:
            dq.append(num)
    return list(dq)