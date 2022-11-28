# [프로그래머스] 피보나치 수
def fibo(n):
    fiboArray = [0] * (n+1)
    fiboArray[0] = 0
    fiboArray[1] = 1
    for i in range(2, n+1):
        fiboArray[i] = fiboArray[i-1] + fiboArray[i-2]
    return fiboArray[n]

def solution(n):
    return fibo(n) % 1234567