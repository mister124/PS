def solution(s):
    answer = True
    stack = []
    for chr in s:
        if chr == '(':
            stack.append(0)
        else:
            if not stack:
                answer = False
                break
            else:
                stack.pop()
    if stack:
        answer = False
    return answer