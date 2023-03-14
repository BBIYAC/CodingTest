# [백준 14938] 서강 그라운드

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
t = list(map(int, input().split()))

graph = [[1e9] * (n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

maxItem = 0
for g in graph:
    count = 0
    for i in range(1, n+1):
        if g[i] <= m:
            count += t[i - 1]
    maxItem = max(maxItem, count)

print(maxItem)