# 모음의 개수
import sys
string = sys.stdin.readline().rstrip()
count = 0
for s in string:
    if s in 'aeiou':
        count += 1
        
print(count)