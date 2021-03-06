'''
게임 개발
N x M 크기의 맵 안에서 게임 캐릭터가 움직이는 시스템

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터
   차례로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음
   왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만
   수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을
   유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 뒤쪽 방향이 바다인 칸이라 뒤로 갈
   수 없는 경우에는 움직임을 멈춘다.

위 매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램

# 입력 조건
1. 첫째 줄에 맵의 세로 크기 N과 가로크기 M을 공백으로 구분하여 입력한다. (3<=N, M<=50)
2. 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A,B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 
   주어진다. (0: 북, 1: 동, 2: 남, 3: 서)
3. 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽
   순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외각은 항상 바다(0: 육지, 1: 바다)
4. 처음 캐릭터가 위치한 칸의 상태는 항상 육지

# 출력 조건
첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수 출력

# 입력 예시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

# 출력 예시
3
'''
# 게임 맵 크기
from threading import current_thread


n, m = map(int, input('>> ').split(' ')) 
# 캐릭터 좌표 x, y, 방향 d
x, y, d = map(int, input('>> ').split(' ')) 
# 게임 맵 생성
game_map = []
for i in range(n):
    game_map.append(list(map(int, input('>> ').split(' '))))
# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1

def solution():
    global x, y, d
    count = 1
    turn_time = 1
    while(True):
        # 왼쪽으로 회전
        turn_left()
        # 전진 가능하면 전진(앞이 육지(0)면)
        if (game_map[x+dx[d]][y+dy[d]] == 0):
            # 기존 위치는 1로 변경
            game_map[x][y] = 1
            # 이동한 위치로 현재 좌표 변경
            x += dx[d]
            y += dy[d]
            count += 1
            turn_time = 1
        else:
            # 방향 회전 수 카운트
            turn_time += 1
            # 모든 방향이 바다(1)이면 종료
            if(turn_time == 4):
                break
    return count

print(solution())