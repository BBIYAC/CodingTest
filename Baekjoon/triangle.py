# 직각 삼각형
'''
문제
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

입력
입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 
각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

출력
각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.

예제 입력 1
6 8 10
25 52 60
5 12 13
0 0 0

예제 출력 1
right
wrong
right
'''

import sys
input = sys.stdin.readline

# 직각 삼각형이 맞는지 판별
def right_triangle(a, b, c):
    # a가 빗변이라면
    a_right = a**2 == b**2 + c**2
    # b가 빗변이라면
    b_right = b**2 == a**2 + c**2
    # c가 빗변이라면
    c_right = c**2 == a**2 + b**2
    return True if a_right or b_right or c_right else False

while(1):
    a, b, c = map(int, input().split())
    if a==0:
        break
    print("right" if right_triangle(a, b, c) else "wrong")