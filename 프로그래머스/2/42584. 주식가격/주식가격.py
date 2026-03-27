def solution(prices):
    stack = []
    answer = [0 for _ in range(len(prices))]
    for idx, num in enumerate(prices):
        if not stack:
            stack.append([idx,num])
            continue
        if num >= stack[-1][1]:
            stack.append([idx,num])
        else:
            while num < stack[-1][1]:
                i, n = stack.pop()
                answer[i] = idx - i
                if not stack:
                    break
            stack.append([idx, num])
    for idx, num in stack:
        answer[idx] = len(prices) - idx -1
    return answer