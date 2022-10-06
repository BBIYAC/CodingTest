# [백준 1463] 1로 만들기
import sys
N = int(sys.stdin.readline().rstrip())
DP = [0]*(N+1)

for i in range(2, N+1):
    DP[i] = DP[i-1] + 1
    if i % 2 == 0 and i % 3 == 0:
        DP[i] = min(DP[i//2] + 1, DP[i//3] + 1)
    elif i % 2 == 0:
        DP[i] = min(DP[i], DP[i//2] + 1)
    elif i % 3 == 0:
        DP[i] = min(DP[i], DP[i//3] + 1)

print(DP[N])