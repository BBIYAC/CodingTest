# [백준 2748] 피보나치 2
import sys

n = int(sys.stdin.readline().rstrip())
fibo = [0]*(n+1)

fibo[0] = 0
fibo[1] = 1
for i in range(2, n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
    
print(fibo[n])