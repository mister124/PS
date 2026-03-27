def solution(name):
    answer = 0
    min_move = len(name) - 1 
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        min_move = min(
            min_move,
            i * 2 + len(name) - next_i, 
            (len(name) - next_i) * 2 + i
        )
    answer += min_move
    return answer