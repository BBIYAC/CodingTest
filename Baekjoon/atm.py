# ATM
'''
5
3 1 4 3 2

32
'''
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = sorted(list(map(int, input().split())))
answer = 0
for i in range(n):
    answer += sum(arr[:i+1])
print(answer)
