# 피보나치의 수
import sys
n = int(sys.stdin.readline().rstrip())
fibo = [0]*(n+1)
for i in range(n+1):
    if i <= 1:
        fibo[i] = i
    else:
        fibo[i] = fibo[i-1]+fibo[i-2]
print(fibo[n])