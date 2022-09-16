# 알고리즘 피보나치 - 재귀, 동적 계획법 비교
import sys
n = int(sys.stdin.readline().rstrip())

# 재귀
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 동적 계획법
def fibonacci(n):
    count = 0
    fibo_dynamic = [0]*(n+1)
    fibo_dynamic[1] = 1
    fibo_dynamic[2] = 1
    for i in range(3, n+1):
        count += 1
        fibo_dynamic[i] = fibo_dynamic[i-1] + fibo_dynamic[i-2]
    return [fibo_dynamic[n], count]

print(*fibonacci(n))