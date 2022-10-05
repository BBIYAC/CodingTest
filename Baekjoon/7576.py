# [백준 7576] 토마토
from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
tomato = []

def bfs(list):
    q = deque(list)
    max_num = 0
    for y, x in list:
        visited[y][x] = 1
    count = 0
    while q:
        count += 1
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0 and box[ny][nx] == 0:
                visited[ny][nx] += visited[cy][cx] + 1
                q.append((ny, nx))
                if visited[ny][nx] > max_num:
                    max_num = visited[ny][nx]
    
    # 토마토가 모두 익지는 못하는 상황이면 -1
    for v in visited:
        if v.count(0) > 0:
            return -1
    # 저장될 때부터 모든 토마토가 익어있는 상태이면 0
    if len(list) == count:
        return 0
    # 모든 토마토가 익는 최소 날짜
    return max_num - 1
                
for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            tomato.append((y, x))
        elif box[y][x] == -1:
            visited[y][x] = -1

print(bfs(tomato))