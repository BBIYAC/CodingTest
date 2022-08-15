# 2007년
'''
문제
오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 
참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

출력
첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.
'''
import sys
x, y = map(int, sys.stdin.readline().split())
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
mmdd = {31: (1, 3, 5, 7, 8, 10, 12), 30: (4, 6, 9, 11), 28: 2}
answer = 0 # 월을 일수로 변환하여 총 일수 구하기

# 월 계산
for month in range(1, x):
    if month in mmdd[31]:
        answer += 31
    elif month in mmdd[30]:
        answer += 30
    else:
        answer += 28
# 일 계산
answer += y

print(days[answer % 7])    
