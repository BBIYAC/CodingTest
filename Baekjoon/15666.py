# [백준 15666] N과 M 12

from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_arr = sorted(map(int, input().split()))

for comb_replace in sorted(set(combinations_with_replacement(N_arr, M))):
    print(*comb_replace)