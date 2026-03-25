def solution(genres, plays):
    dict_gp = dict()
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dict_gp:
            dict_gp[g] = []
        dict_gp[g].append((p, i))
    for g in dict_gp:
        dict_gp[g].sort(key=lambda x: (-x[0], x[1]))
    dict_sg = [(sum(x[0] for x in dict_gp[g]), g) for g in dict_gp.keys()]
    dict_sg.sort(reverse=True) 
    answer = []
    for total_play, g in dict_sg:
        for play, idx in dict_gp[g][:2]:
            answer.append(idx)
    return answer