import sys

input = sys.stdin.readline
N = int(input())
exam_score = list(map(int, input().split()))
max_score = max(exam_score)
print(sum(exam_score) / max_score * 100 / N)
