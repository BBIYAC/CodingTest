# [백준 12904] A 와 B
import sys
S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

answer = 1
while True:
    if len(T) == len(S):
        if T != S:
            answer = 0
        break
    # 방법 1. 문자열 뒤에 A 추가 -> T 마지막 값 제거
    if T[-1] == 'A':
        T = T[:-1]
    else: # 방법 2. 문자열 뒤집은 후 뒤에 B 추가 -> T에서 B제거 후 뒤집기
        T = T[-2::-1]

print(answer)