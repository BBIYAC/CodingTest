# [백준 10833] 사과
import sys
input = sys.stdin.readline

N = int(input().rstrip())
answer = 0
for _ in range(N):
    student, apple = map(int, input().split())
    answer += apple % student

print(answer)