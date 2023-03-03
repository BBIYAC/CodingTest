# [백준 1158] 요세푸스 문제

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

answer = []
idx = 0

for _ in range(N):
    idx += K-1
    idx = idx%len(arr)
    answer.append(str(arr.pop(idx)))

print('<', ', '.join(answer)[:], '>', sep='')