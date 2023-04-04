# [백준 15664] N과 M 10

from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_arr = sorted(map(int, input().split()))

# 조합
for comb in sorted(set(combinations(N_arr, M))):
    print(*comb)