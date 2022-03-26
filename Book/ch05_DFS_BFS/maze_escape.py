'''
미로 탈출
NxM크기의 미로 탈출
현 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동 가능
괴물이 있는 부분은 0, 괴물이 없는 부분은 1
탈출하기 위해 움직여야 하는 최소 칸의 개수

# 입력 조건
첫째 줄에 두 정수 N, M을 입력받고, N개의 줄에는 각각 M개의 정수가 공백없이 제시됨

# 출력 조건
최소 이동 칸의 개수 출력

# 입력 예시
5 6
101010
111111
000001
111111
111111

# 출력 예시
10

# BSF(너비 우선 탐색)
가까운 노드부터 탐색하는 알고리즘
큐(queue) 사용
'''
from collections import deque
import queue

# 맵 크기 N, M 입력
n, m = map(int, input('>> ').split())

# 미로 정보 입력(괴물 0, 노괴물 1)
maze = []
for i in range(n):
    maze.append(list(map(int, input('>> '))))

# 상, 하, 좌, 우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(x, y):
    # 양방향 큐 데크(deque) 선언
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x+dx[i] # 다음 x 위치
            ny = y+dy[i] # 다음 y 위치
            # 미로 맵을 벗어난 경우, 벽인 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m or maze[nx][ny]==0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y]+1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return maze[n-1][m-1]

print(solution(0, 0))