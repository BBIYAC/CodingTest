# [백준 7562] 나이트의 이동
from collections import deque
import sys
input = sys.stdin.readline

# 테스트 케이스 t
t = int(input().rstrip())
for _ in range(t):
    # 체스판 한 변의 길이 l
    l = int(input().rstrip())
    visited = [[0]*l for _ in range(l)]
    # 나이트가 현재 있는 칸 (sy, sx)
    sy, sx = map(int, input().split())
    # 나이트가 이동하려는 칸 (ey, ex)
    ey, ex = map(int, input().split())
    # bfs 탐색
    q = deque()
    q.append((sy, sx))
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    while q:
        cy, cx = q.popleft()
        if (cy, cx) == (ey, ex):
            break
        for i in range(8):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= nx < l and 0 <= ny < l and visited[ny][nx] == 0:
                visited[ny][nx] = visited[cy][cx] + 1
                q.append((ny, nx))
    print(visited[ey][ex])