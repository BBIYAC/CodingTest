# [백준 2845] 파티가 끝나고 난 뒤

import sys
input = sys.stdin.readline

L, P = map(int, input().split())
arr = list(map(int, input().split()))

for N in arr:
    print(N - (L * P), end=' ')