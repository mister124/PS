from collections import deque
def solution(priorities, location):
    answer = 1
    p = deque(priorities)
    cnt = 0
    while p:
        if p[0] == max(p):
            p.popleft()
            cnt += 1
            if location == 0:
                answer = cnt
                break
            else:
                location -= 1
        else:
            p.rotate(-1)
            if location == 0:
                location = len(p) - 1
            else:
                location -= 1
    return answer