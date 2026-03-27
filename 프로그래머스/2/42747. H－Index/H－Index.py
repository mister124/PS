from bisect import bisect_left
def solution(citations):
    c_list = sorted(citations)
    left = 0
    right = len(citations)
    answer = 0
    while left <= right:
        mid = (left+right) // 2
        index = bisect_left(c_list,mid)
        h = len(c_list) - index
        if h >= mid:
            answer = max(mid,answer)
            left = mid +1
        else:
            right = mid -1
    return answer