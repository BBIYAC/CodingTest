'''
연구소
N x M 크기의 연구소에서 바이러스가 퍼지지 않도록 벽 3개를 세운다.
0은 빈칸, 1은 벽, 2는 바이러스
연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역의 크기의 최댓값

# 입력 조건
1. 세로 N, 가로 M
2. N개의 줄에 지도 모양
3. 빈칸의 개수는 3개 이상

# 출력 조건
얻을 수 있는 안전 영역의 최대 크기

# 입력 예시 1
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

# 출력 예시 1
27

# 입력 예시 2
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

# 출력 예시 2
9

# 입력 예시 3
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

# 출력 예시 3
3
'''
    

# 정답

answer = 0
def answer_solution():
    n, m = map(int, input('>> ').split())
    data = [] # 초기 맵 리스트
    temp = [[0]*m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

    for _ in range(n):
        data.append(list(map(int, input('>> ').split())))

    # 4가지 이동 방향에 대한 리스트
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
    def virus(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if temp[nx][ny] == 0:
                    # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                    temp[nx][ny] = 2
                    virus(nx, ny)

    # 현재 맵에서 안전 영역의 크기 계산 메서드
    def get_score():
        score = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    score += 1
        return score

    # 깊이 우선 탐색을 이용해 울타리 설치 및 안전 영역 크기 계산
    def dfs(count):
        global answer
        # 울타리가 3개 설치된 경우
        if count == 3:
            for i in range(n):
                for j in range(m):
                    temp[i][j] = data[i][j]
            # 각 바이러스의 위치에서 전파 진행
            for i in range(n):
                for j in range(m):
                    if temp[i][j] == 2:
                        virus(i, j)
            # 안전 영역 최댓값 계산
            answer = max(answer, get_score())
            return
        # 빈 공간에 울타리 설치
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    data[i][j] = 1
                    count += 1
                    dfs(count)
                    data[i][j] = 0
                    count -= 1

    dfs(0)
    return answer

print(answer_solution())