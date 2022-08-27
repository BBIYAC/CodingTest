# 대소문자 변환
import sys
string = sys.stdin.readline().rstrip()
answer = ''
for s in string:
    if s.isupper():
        answer += s.lower()
    else:
        answer += s.upper()
print(answer)