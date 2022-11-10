# [프로그래머스] 게임 맵 최단거리
from collections import deque

def bfs(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] += 1
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and maps[ny][nx] == 1:
                visited[ny][nx] = visited[cy][cx] + 1
                queue.append((ny, nx))
    return visited[n - 1][m - 1]
    
def solution(maps):
    answer = bfs(maps)
    return answer if answer else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1