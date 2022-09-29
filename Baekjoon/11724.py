# [백준 11724] 연결 요소의 개수
import sys
input = sys.stdin.readline
# 정점의 개수 N, 간선의 개수 M
N, M = map(int, input().split())
dots = {}
for _ in range(M):
    s, e = map(int, input().split())
    # 인덱스 에러 방지를 위해 -1
    if s-1 in dots:
        dots[s-1].append(e-1)
    else:
        dots[s-1] = [e-1]
    if e-1 in dots:
        dots[e-1].append(s-1)
    else:
        dots[e-1] = [s-1]

visited = [False]*N

def bfs(v):
    q = [v]
    visited[v] = True
    while q:
        c = q.pop(0)
        if c not in dots:
            continue
        for n in dots[c]:
            if visited[n] == False:
                visited[n] = True
                q.append(n)

# 연결 지점이 끊길 때마다 카운트
count = 0
for i in range(N):
    if visited[i] == False:
        bfs(i)
        count += 1

print(count)