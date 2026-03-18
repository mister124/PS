import sys
input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))  # 끝 시간, 시작 시간 순 정렬

count = 0
end = 0
for start, finish in meetings:
    if start >= end:
        count += 1
        end = finish

print(count)