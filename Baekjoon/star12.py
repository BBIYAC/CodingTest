# 별찍기 12
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1, n+1):
    print(' '*(n-i) + '*'*i)
for i in range(1, n):
    print(' '*i + '*'*(n-i))