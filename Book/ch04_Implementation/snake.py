'''
뱀
게임은 N x N 정사각 보드 위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다.
보드의 상하좌우 끝에는 벽이 있다.
게임을 시작할 때 뱀은 맨 위 맨 좌측에 위치하고 길이는 1이다.
벽 또는 자기 자신의 몸과 부딪히면 게임이 끝남.

규칙
1. 뱀은 몸 길이를 늘려 머리를 다음 칸에 위치시킴
2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
3. 만약 이동한 칸에 사과가 없다면, 몸 길이를 줄여 꼬리가 위치한 칸을 비워줌.

# 입력 조건
1. 첫째 줄에 보드의 크기 N
2. 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미함
3. 다음 줄에는 뱀의 방향 변환 횟수 L이 주어짐
4. 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며,
   게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')으로 90도 회전

# 출력 조건
게임이 몇 초에 끝나는 지 출력

# 입력 예시 1
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

# 출력 예시 1
9

# 입력 예시 2
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

# 출력 예시 2
21

# 입력 예시 3
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L

# 출력 예시 3
13
'''

# def solution():
#     time = 0
#     # 보드의 크기
#     n = int(input('>> '))
#     # 사과의 개수
#     k = int(input('>> '))
#     # 사과의 위치
#     board = [[0]*n for _ in range(n)]
#     for _ in range(k):
#         r, c = map(int, input('>> ').split())
#         board[r-1][c-1] = 1

#     for i in range(n):
#         print(board[i])

#     # 방향 전환 횟수 
#     l = int(input('>> '))
#     # 방향 전환 정보
#     for _ in range(l):
#         x, c = input('>> ').split()
#         time += int(x)
        
#     return time

# print(solution())


# 정답
def turn(direction, c):
    if c== 'L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

def answer_solution():
    n = int(input('>> '))
    k = int(input('>> '))
    data = [[0]*(n+1) for _ in range(n+1)] # 맵 정보
    info = [] # 방향 회전 정보

    # 맵 정보
    for _ in range(k):
        a, b = map(int, input('>> ').split())
        data[a][b] = 1

    # 방향 회전 정보 입력
    l = int(input('>> '))
    for _ in range(l):
        t, c = input('>> ').split()
        info.append((int(t), c))

    # 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초'
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while True:
        nx = x+dx[direction]
        ny = y+dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1<=nx and nx<=n and 1<=ny and ny<=n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else: # 벽이나 뱀의 몸통과 부딪혔다면
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리 이동
        time += 1
        if index<1 and time==info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(answer_solution())
