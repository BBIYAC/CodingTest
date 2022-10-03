# [백준 12865] 배낭
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
things = [[0, 0]]
DP = [[0]*(K+1) for _ in range(N+1)]

for _ in range(N):
    things.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        W, V = things[i]

        if j < W:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-W]+V)

print(DP[N][K])