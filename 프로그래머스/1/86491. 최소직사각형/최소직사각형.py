def solution(sizes):
    width, height = 0, 0
    for wh in sizes:
        width = max(width,max(wh))
        height = max(height,min(wh))
    answer = width * height
    return answer