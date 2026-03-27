def solution(k, dungeons):
    answer = [0] 
    visited = [False] * len(dungeons)
    def dfs(current_k, cnt):
        answer[0] = max(answer[0], cnt)
        for i in range(len(dungeons)):
            req_k, use_k = dungeons[i] 
            if not visited[i] and current_k >= req_k:
                visited[i] = True 
                dfs(current_k - use_k, cnt + 1) 
                visited[i] = False 
    dfs(k, 0)
    return answer[0]