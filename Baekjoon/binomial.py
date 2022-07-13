# 이항 계수
'''
문제
자연수 N과 정수 K가 주어졌을 때 이항 계수 binom{N}{K}를 구하는 프로그램을 작성하시오.

입력
첫째줄에 N과 K가 주어진다.

출력
이항 계수 binom{N}{K}를 출력한다.

예제 입력 1
5 2

예제 출력 1
10
'''

import sys

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

# 자연수 N과 정수 K
n, k = map(int, sys.stdin.readline().split())
# 이항 계수 점화식 n!/k!(n-1)!
print(factorial(n) // (factorial(k)*factorial(n-k)))
