'''
인구 이동
각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는지 구하는 프로그램
- 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
- 위의 조건에 의해 열어야 하는 국경선이 모두 열렸다면, 인구 이동 시작
- 국경선이 열려 있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
- 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수)/(연합을 이루고 있는 칸의 개수), 소수점 버림
- 연합을 해체하고, 모든 국경선을 닫는다.

# 입력 예시 1
2 20 50
50 30
20 40

# 출력 예시 1
1

# 입력 예시 2
2 40 50
50 30
20 40

# 출력 예시 2
0

# 입력 예시 3
2 20 50
50 30
30 40

# 출력 예시 3
1

# 입력 예시 4
3 5 10
10 15 20
20 30 25
40 22 10

# 출력 예시 4
2

# 입력 예시 5
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10

# 출력 예시 5
3
'''
# 정답

from collections import deque


n, l, r = map(int, input('>> ').split())
board = []
for i in range(n):
    board.append(list(map(int, input('>> ').split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = board[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x,y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += board[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구 분배
    for i, j in united:
        board[i][j] = summary // count
    return count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n*n:
        break
    total_count += 1

def answer_solution():
    count = total_count
    return count

print(answer_solution())