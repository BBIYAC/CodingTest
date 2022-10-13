# [백준 1389] 케빈 베이컨의 6단계 법칙
from collections import deque
import sys
input = sys.stdin.readline

# 유저의 수 N, 친구 관계의 수 M
N, M = map(int, input().split())
relationship = [[] for _ in range(N+1)]

for _ in range(M):
    # 친구 관계
    A, B = map(int, input().split())
    relationship[A].append(B)
    relationship[B].append(A)

def bfs(s):
    visited = [0]*(N+1)
    q = deque()
    q.append(s)
    while q:
        c = q.popleft()
        for r in relationship[c]:
            if visited[r] == 0:
                visited[r] = visited[c] + 1
                q.append(r)
    return sum(visited) - visited[s]

min_value = [1e9, 0]
for i in range(1, N+1):
    result = bfs(i)
    if result < min_value[0]:
        min_value = [result, i]

print(min_value[1])