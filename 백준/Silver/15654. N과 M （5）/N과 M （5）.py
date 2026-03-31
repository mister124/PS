import sys

input = sys.stdin.readline
N, M = map(int, input().split())

# 1. 입력받은 숫자들을 정수로 변환 후 오름차순 정렬
num = sorted(list(map(int, input().split())))
visited = [False] * N
stack = []

def backtracking(depth):
    # 2. M개를 모두 선택했을 경우 출력 (리스트 압축 풀기)
    if depth == M:
        print(*stack)
        return
        
    prev = 0  # 중복 수열 출력을 방지하기 위한 변수
    
    for i in range(N):
        # 3. 방문하지 않았고, 현재 깊이에서 방금 사용한 숫자가 아닌 경우에만 탐색
        if not visited[i] and prev != num[i]:
            visited[i] = True
            stack.append(num[i])
            prev = num[i]
            
            backtracking(depth + 1)
            
            # 4. 탐색 종료 후 상태 원상 복구
            stack.pop()
            visited[i] = False

backtracking(0)