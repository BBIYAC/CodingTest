# 네 번째 점
'''
문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.

예제 입력 1
5 5
5 7
7 5

예제 출력 1
7 7

예제 입력 2
30 20
10 10
10 20

예제 출력 2
30 10
'''

import sys
input = sys.stdin.readline

# 네 번째 점
fx, fy = list(), list()
# 세 개의 점 좌표
for _ in range(3):
    x, y = map(int, input().split())
    fx.remove(x) if x in fx else fx.append(x)
    fy.remove(y) if y in fy else fy.append(y)

print(fx[0], fy[0])
