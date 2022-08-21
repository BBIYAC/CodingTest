# 전자레인지
import sys
num = int(sys.stdin.readline().rstrip())
second = num
answer = []
# a = 5min = 300s, b = 1min = 60s, c = 10s
a, b, c = 300, 60, 10

if second >= a:
    answer.append(second//a)
    second %= a
else:
    answer.append(0)
if second >= b:
    answer.append(second//b)
    second %= b
else:
    answer.append(0)
if second >= c:
    second //= c
    answer.append(second)
else:
    answer.append(0)
if num == a*answer[0]+b*answer[1]+c*answer[2]:
    print(*answer)
else:
    print(-1)