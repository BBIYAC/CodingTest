# [백준 15657] N과 M 8

from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_arr = sorted(list(map(int, input().split())))

# 중복 조합
for prod in combinations_with_replacement(N_arr, M):
    print(*prod)