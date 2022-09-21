# [백준 2178] 미로 찾기
import sys
input = sys.stdin.readline

# 세로 N, 가로 M
N, M = map(int, input().split())
# N x M인 미로
graph = [input().rstrip() for _ in range(N)]

def bfs(n, m):
    # 처음 시작 칸은 (1, 1) => 인덱스로 (0, 0)
    queue = [(0, 0)]
    # 방문 여부 & 이동거리
    visited = [[0]*M for _ in range(N)]
    # 첫 번째 칸
    visited[0][0] = 1
    # 네 방향
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    while queue:
        # 현재 위치
        cy, cx = queue.pop(0)
        # 네 방향 탐색
        for i in range(4):
            # 다음 위치
            ny = cy + dy[i]
            nx = cx + dx[i]
            # 미로 안에 있으면서 방문하지 않았고 갈 수 있는 길(1)인 경우
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and graph[ny][nx] == '1':
                # 현재 이동 거리 수 + 1
                visited[ny][nx] += visited[cy][cx] + 1
                # 다음 탐색을 위해 큐에 추가
                queue.append((ny, nx))
    # 목적지까지의 이동 거리
    return visited[n][m]

# 인덱스 때문에 각각 -1
print(bfs(N-1, M-1))