# [백준 17626] Four Squares

import sys
input = sys.stdin.readline

N = int(input().rstrip())

def fourSquares(N):
    # N이 제곱근일 때
    if int(N**0.5) == N**0.5:
        return 1

    # N이 2개의 제곱근으로 이루어져 있을 때
    for i in range(1, int(N**0.5) + 1):
        if int((N-(i*i))**0.5) == (N-(i*i))**0.5:
            return 2
        
    # N이 3개의 제곱근으로 이루어져 있을 때
    for i in range(1, int(N**0.5) + 1):
        for j in range(1, int((N-(i*i))**0.5 + 1)):
            if int((N - (i*i) - (j*j))**0.5) == (N - (i*i) - (j*j))**0.5:
                return 3

    # 그 외의 나머지 경우는 4
    return 4

print(fourSquares(N))