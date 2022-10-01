# [백준 1012] 유기농 배추

import sys
input = sys.stdin.readline

def bfs(y, x):
    q = [(y, x)]
    visited[y][x] = True
    while q:
        cy, cx = q.pop(0)
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == False and field[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((ny, nx))


T = int(input().rstrip())
for _ in range(T):
    # 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and field[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)