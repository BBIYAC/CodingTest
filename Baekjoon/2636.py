# [백준 2636] 치즈
from collections import deque
import sys
input = sys.stdin.readline

r, c  = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    visited = [[False]*c for _ in range(r)]
    count = 0
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= nx < c and 0 <= ny < r and visited[ny][nx] == False:
                if board[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append([ny, nx])
                elif board[ny][nx] == 1:
                    board[ny][nx] = 0
                    count += 1
                    visited[ny][nx] = True
    return count

time, cheese = 0, []
while True:
    time += 1
    cheese.append(bfs())
    if cheese[-1] == 0:
        break

print(time-1)
print(cheese[-2])