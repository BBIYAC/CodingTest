# [백준 15655] N과 M 6

from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_arr = sorted(list(map(int, input().split())))

for comb in combinations(N_arr, M):
    print(*comb)