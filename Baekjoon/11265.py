# [백준 11265] 끝나지 않는 파티

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
party = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if party[i][j] > party[i][k] + party[k][j]:
                party[i][j] = party[i][k] + party[k][j]

for _ in range(M):
    A, B, C = map(int, input().split())
    print('Stay here' if party[A-1][B-1] > C else 'Enjoy other party')