# 파도반 수열
import sys
T = int(sys.stdin.readline().rstrip())

DP = [0]*101

for i in range(1, 101):
    DP[i] = 1 if i <= 3 else DP[i-2] + DP[i-3]

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(DP[N])