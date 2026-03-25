def solution(clothes):
    kind = set()
    d = dict()
    for arr in clothes:
        if arr[1] not in kind:
            kind.add(arr[1])
            d[arr[1]] = []
        d[arr[1]].append(arr[0])
    count = [len(val) + 1 for val in d.values()]
    answer = 1
    for i in count:            
        answer *= i
    answer -= 1
    return answer