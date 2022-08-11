# 별 찍기 4
import sys
input = sys.stdin.readline

n = int(input().rstrip())
for i in range(n):
    print(' '*i + '*'*(n-i))