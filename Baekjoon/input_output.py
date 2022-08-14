# 입력받은 그대로 출력하기
import sys
while 1:
    s = sys.stdin.readline().rstrip()
    if s:
        print(s)
    else:
        break