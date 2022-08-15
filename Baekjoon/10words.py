# 10개씩 끊어 출력하기
import sys
s = sys.stdin.readline().rstrip()
for i in range(0, len(s), 10):
    print(s[i:i+10])