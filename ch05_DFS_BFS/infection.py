'''
경쟁적 전염
N x N 크기의 시험관, 바이러스의 종류는 1~K
1초마다 상, 하, 좌, 우의 방향으로 증식, 매 초 번호가 낮은 종류의 바이러스부터 먼저 증식
이미 해당 칸에 바이러스가 있다면 다른 바이러스 X

시험관의 크기와 바이러스의 위치 정보가 주어졌을 때,  S초가 지난 후에 (X, Y)에 존재하는 바이러스의
종류를 출력하는 프로그램

# 입력 조건
1. 자연수N, K
2. N개의 줄에 걸쳐 시험관의 정보
3. N+2번째 줄에는 S, X, Y가 주어지며 공백으로 구분

# 출력 조건
S초 뒤에 (X, Y)에 존재하는 바이러스의 종류 출력
해당 위치에 바이러스가 없다면 0

# 입력 예시 1
3 3
1 0 2
0 0 0
3 0 0
2 3 2

# 출력 예시 1
3

# 입력 예시 2
3 3
1 0 2
0 0 0
3 0 0
1 2 2

# 출력 예시 2
0
'''

# 너비 우선 탐색 활용
from collections import deque

def answer_solution():
    n, k = map(int, input('>> ').split())
    graph = [] # 전체 보드 정보를 담는 리스트
    data = [] # 바이러스에 대한 정보를 담는 리스트

    for i in range(n):
        # 보드 정보를 한 줄 단위로 입력
        graph.append(list(map(int, input('>> ').split())))
        for j in range(n):
            # 해당 위치에 바이러스가 존재하는 경우
            if graph[i][j] != 0:
                # 바이러스 종류, 시간, 위치 삽입
                data.append((graph[i][j], 0, i, j))

    # 정렬 이후 큐로 옮기기
    q = deque(sorted(data))

    target_s, target_x, target_y = map(int, input('>> ').split())

    # 바이러스가 퍼져나갈 수 있는 4가지 위치
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 너비 우선 탐색 진행
    while q:
        virus, s, x, y = q.popleft()
        # 정확히 S초가 지나거나, 큐가 빌 때까지 반복
        if s == target_s:
            break
        
        # 현재 노드에서 주변 4가지 위치를 각각 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 해당 위치로 이동할 수 있는 경우
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    q.append((virus, s+1, nx, ny))
    answer = graph[target_x-1][target_y-1]
    return answer

print(answer_solution())