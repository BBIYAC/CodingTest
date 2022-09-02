# 보물
'''
5
1 1 1 6 0
2 7 8 3 1

18
'''
import sys
input = sys.stdin.readline

n = int(input().rstrip())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))

S = 0
for i in range(n):
    b = max(B)
    S += A[i]*b
    B.remove(b)

print(S)