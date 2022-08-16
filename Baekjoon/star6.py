# 별찍기 6
import sys
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    print(' '*i + '*'*(2*(N-i)-1))
for i in range(2, N+1):
    print(' '*(N-i)+'*'*(2*i-1))