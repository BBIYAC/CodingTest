# [백준 20057] 마법사 상어와 토네이도
# import sys
# input = sys.stdin.readline

# N = int(input().rstrip())
# data = [list(map(int, input().split())) for _ in range(N)]

# # 모래이동
# def moveSand(prev, y, x, d):
#     sand = 0
#     percent1 = int(prev*0.01)
#     percent2 = int(prev*0.02)
#     percent5 = int(prev*0.05)
#     percent7 = int(prev*0.07)
#     percent10 = int(prev*0.1)
#     return sand

# cy, cx = N//2, N//2
# count = 0
# for i in range(1, N+1):
#     # 홀수이면 왼쪽, 아래 방향
#     if i % 2 != 0:
#         # 왼쪽
#         count += moveSand(data[cy][cx], cy, cx-i, 'left')
#         cx -= i
#         # 아래쪽
#         count += moveSand(data[cy][cx], cy-i, cx, 'down')
#         cy -= i
#     else: # 짝수이면 오른쪽, 위 방향 
#         # 오른쪽
#         count += moveSand(data[cy][cx], cy, cx+i, 'right')
#         cx += i
#         # 위쪽
#         count += moveSand(data[cy][cx], cy+i, cx, 'up')
#         cy += i


# 모래 계산하는 함수
def recount(time, dx, dy, direction):
    global ans, s_x, s_y

    # y좌표 계산 & x좌표 갱신
    for _ in range(time):
        s_x += dx
        s_y += dy
        if s_y < 0:  # 범위 밖이면 stop
            break

        # 3. a, out_sand
        total = 0  # a 구하기 위한 변수
        for dx, dy, z in direction:
            nx = s_x + dx
            ny = s_y + dy
            if z == 0:  # a(나머지)
                new_sand = sand[s_x][s_y] - total
            else:  # 비율
                new_sand = int(sand[s_x][s_y] * z)
                total += new_sand

            if 0 <= nx < N and 0 <= ny < N:   # 인덱스 범위이면 값 갱신
                sand[nx][ny] += new_sand
            else:  # 범위 밖이면 ans 카운트
                ans += new_sand


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

# 2. 방향별 모래 비율 위치
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

s_x, s_y = N//2, N//2  # 시작좌표(x좌표)
ans = 0  # out_sand

# 1.토네이도 회전 방향(y위치)
for i in range(1, N + 1):
    if i % 2:
        recount(i, 0, -1, left)
        recount(i, 1, 0, down)
    else:
        recount(i, 0, 1, right)
        recount(i, -1, 0, up)

print(ans)
