def solution(nums):
    nums_set = set(nums)
    limit = len(nums) // 2
    answer = min(len(nums_set), limit)
    return answer
    