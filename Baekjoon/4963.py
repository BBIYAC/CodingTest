# [백준 4963] 섬의 개수
import sys
input = sys.stdin.readline

def bfs(y, x):
    visited[y][x] = True
    q = [(y, x)]
    while q:
        cy, cx = q.pop(0)
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < w and 0 <= ny < h and visited[ny][nx] == False and maps[ny][nx] == '1':
                visited[ny][nx] = True
                q.append((ny, nx))

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0): break
    maps = [input().split() for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    count = 0

    for y in range(h):
        for x in range(w):
            if visited[y][x] == False and maps[y][x] == '1':
                bfs(y, x)
                count += 1

    print(count)