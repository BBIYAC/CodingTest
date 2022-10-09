# [백준 2584] 영역 구하기
from collections import deque
import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
visited = [[False]*N for _ in range(M)]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    count = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[ny][nx] == False:
                count += 1
                q.append((ny, nx))
                visited[ny][nx] = True
    return count

for _ in range(K):
    LDX, LDY, RUX, RUY = map(int, input().split())
    for y in range(LDY, RUY):
        for x in range(LDX, RUX):
            if visited[y][x] == False:
                visited[y][x] = True

answer = []   
for i in range(M):
    for j in range(N):
        if visited[i][j] == False:
            answer.append(bfs(i, j))

print(len(answer))
print(*sorted(answer))