from collections import deque
def solution(progresses, speeds):
    p = deque(progresses)
    s = deque(speeds)
    answer = []
    while p:
        for i in range(len(p)):
            p[i] = min(100,p[i] +s[i])
        cnt = 0
        while p and p[0] == 100:
            p.popleft()
            s.popleft()
            cnt += 1
        if cnt:
            answer.append(cnt)
    return answer