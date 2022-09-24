# 수 찾기
import sys
input = sys.stdin.readline

N = int(input().rstrip())
N_set = set(map(int, input().split()))
M = int(input().rstrip())
M_arr = map(int, input().split())

for find in M_arr:
    if find in N_set:
        print(1)
    else:
        print(0)