# 진법 변환 5
import sys
N, B = map(int, sys.stdin.readline().split())
answer = ''
while N:
    mod = N % B
    if mod >= 10:
        answer += chr(65 + (mod - 10))
    else:
        answer += str(mod)
    N //= B

print(answer[::-1])