# 평균 점수
import sys

answer = 0
for _ in range(5):
    n = int(sys.stdin.readline().rstrip())
    if n < 40:
        answer += 40
    else:
        answer += n
        
print(answer//5)