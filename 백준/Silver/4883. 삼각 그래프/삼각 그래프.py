import sys

input = sys.stdin.readline
tc = 1

while True:
    N = int(input())
    if N == 0:
        break
        
    nodes = [list(map(int, input().split())) for _ in range(N)]
    
    # 0행 초기화: 무조건 (0, 1)에서 시작하므로 (0, 0)은 도달 불가 처리
    nodes[0][0] = float('inf')
    nodes[0][2] += nodes[0][1]
    
    # 1행부터 N-1행까지 DP 탐색
    for i in range(1, N):
        # 1. 왼쪽 열 갱신
        nodes[i][0] += min(nodes[i-1][0], nodes[i-1][1])
        
        # 2. 가운데 열 갱신 (갱신된 nodes[i][0] 사용)
        nodes[i][1] += min(nodes[i][0], nodes[i-1][0], nodes[i-1][1], nodes[i-1][2])
        
        # 3. 오른쪽 열 갱신 (갱신된 nodes[i][1] 사용)
        nodes[i][2] += min(nodes[i][1], nodes[i-1][1], nodes[i-1][2])
        
    # 출력 형식에 맞춰 최단 거리 출력
    print(f"{tc}. {nodes[N-1][1]}")
    tc += 1