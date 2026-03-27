from collections import deque
def solution(answers):
    a = deque([1,2,3,4,5])
    b = deque([2,1,2,3,2,4,2,5])
    c = deque([3,3,1,1,2,2,4,4,5,5])
    ac = bc = cc = 0
    for answer in answers:
        if a[0] == answer:
            ac += 1
        a.rotate(-1)
        if b[0] == answer:
            bc += 1
        b.rotate(-1)
        if c[0] == answer:
            cc += 1
        c.rotate(-1)
    val = max(ac,bc,cc)
    answer = []
    if ac == val:
        answer.append(1)
    if bc == val:
        answer.append(2)
    if cc == val:
        answer.append(3)
    return answer