def solution(brown, yellow):
    total = brown+yellow
    temp = set()
    answer = []
    for i in range(1,total+1):
        if total % i == 0:
            temp.add(i)
    for i in list(temp):
        j = total // i
        if (i+j) * 2 -4 == brown:
            answer.append(max(i,j))
            answer.append(min(i,j))
            break
    return answer