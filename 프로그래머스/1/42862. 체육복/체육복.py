def solution(n, lost, reserve):
    student = [x for x in range(1,n+1)]
    student_l = set(lost)
    student_r = set(reserve)
    l_r = student_l & student_r
    student_r = student_r - l_r
    student_l = student_l - l_r
    for s in student:
        if s in student_r:
            if s-1 in student_l:
                student_l.remove(s-1)
            elif s+1 in student_l:
                student_l.remove(s+1)
                continue
    return n - len(student_l)