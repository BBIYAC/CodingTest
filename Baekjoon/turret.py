# 터렛
'''
문제
조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 
조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 
류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.
한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. 
x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.

출력
각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 
만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.

예제 입력 1
3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5

예제 출력 1
2
1
0
'''

from math import sqrt
import sys
input = sys.stdin.readline

# 테스트 케이스 수 T
t = int(input().strip())
for _ in range(t):
    # 조규현 좌표(X1, Y1), 류재명과의 거리 R1, 백승환 좌표(X2, Y2), 류재명과의 거리 R2
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 중점 사이의 거리 D
    d = sqrt((x1-x2)**2 + (y1-y2)**2)
    # 무수히 많은 경우(d = 0 and r1 = r2)
    if d == 0 and r1 == r2:
        print(-1)
    # 만나지 않는 경우(d > r1+r2 or d < |r1-r2|)
    elif d > r1+r2 or d < abs(r1-r2):
        print(0)
    # 한 점에서 만나는 경우(외접 : d = r1+r2 or 내접 : d = |r1-r2|)
    elif d == r1+r2 or d == abs(r1-r2):
        print(1)
    # 두 점에서 만나는 경우(d < r1+r2)
    elif d < r1+r2:
        print(2)
