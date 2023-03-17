# [백준 14503] 로봇 청소기

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# space = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, 1]

# visited[r][c] = 1
# count = 1

# while True:
#     clean = 0
#     for _ in range(4):
#         nx = r + dx[(d+3)%4]
#         ny = c + dy[(d+3)%4]
#         d = (d+3) % 4
#         if 0 <= nx < N and 0 <= ny < M and space[nx][ny] == 0 and visited[nx][ny] == 0:
#             visited[nx][ny] = 1
#             count += 1
#             r, c = nx, ny
#             clean = 1
#             break
#     if clean == 0:
#         if space[r-dx[d]][c-dy[d]] == 1:
#             print(count)
#             break
#         else:
#             r, c = r-dx[d], c-dy[d]

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
r,c,d = map(int,input().split())

# d => 0,3,2,1 순서로 돌아야한다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 처음 시작하는 곳 방문 처리
visited[r][c] = 1
cnt = 1

while 1:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        # 0,3,2,1 순서 만들어주기위한 식
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        # 한번 돌았으면 그 방향으로 작업시작
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                #청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break
    if flag == 0: # 4방향 모두 청소가 되어 있을 때,
        if graph[r-dx[d]][c-dy[d]] == 1: #후진했는데 벽
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d]