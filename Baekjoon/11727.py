# [백준 11727] 2 x N 타일링
import sys
N = int(sys.stdin.readline().rstrip())
DP = [0]*(1001)
DP[1] = 1
DP[2] = 3

for i in range(3, N+1):
    DP[i] = DP[i-1] + 2*DP[i-2]

print(DP[N]%10007)