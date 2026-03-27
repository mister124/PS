import heapq
def solution(scoville, K):
    s_h = scoville[:]
    heapq.heapify(s_h)
    cnt = 0
    while s_h[0] < K:
        if len(s_h) == 1:
            cnt = -1
            break
        cnt += 1
        a = heapq.heappop(s_h)
        b = heapq.heappop(s_h) * 2
        heapq.heappush(s_h, a+b)
    answer = cnt
    return answer